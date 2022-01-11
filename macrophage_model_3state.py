# 0 or 2 stepwise effect
# This script consists of a discrete mathematical model (21 3-state nodes, 21 transition functions)
# and code to run the model to obtain steady states.
# External parameters - FUNGUS, FE2, FE3, EHEME - need to be specified a state (0-low, 1-medium or 2-high)
# before running the model.
# FUNGUS state 0 correspond to absent and state 1 or 2 correspond to  present.

#!/usr/bin/python3
import itertools
import random
import sys

FUNGUS = 0
SIGNAL = 1
INIL6 = 2
INTNF = 3
EXIL6 = 4
EXTNF = 5
DMT = 6
TFR1 = 7
ZIP = 8
FT = 9
BDH2 = 10
CYTFPN = 11
MEMFPN = 12
IRP = 13
LIP = 14
FE2 = 15
FE3 = 16
HEP = 17
EHEME = 18
HO1 = 19
NRF2 = 20

NUM_AGENTS = 21

nodes = ['FUNGUS', 'SIGNAL','INIL6', 'INTNF', "EXIL6", 'EXTNF',"DMT", 'TFR1','ZIP','FT','BDH2', 'CYTFPN', 'MEMFPN', 'IRP', 'LIP','FE2', 'FE3', "HEP","EHEME", "HO1", "NRF2"]

class Model():
    def __init__(self):
        self.states = []
    def set_init_states(self, array_of_states):
        self.states = array_of_states
    def update_states(self):
        new = [0] * len(self.states)
        old = self.states

        new[FUNGUS] = 0
        new[SIGNAL] = old[FUNGUS]

        if old[SIGNAL]>=1:
            new[INIL6]=2
        elif old[SIGNAL]==0:
            new[INIL6]=1
        
        if old[SIGNAL]>=1:
            new[INTNF]=2
        elif old[SIGNAL]==0:
            new[INTNF]=1

        new[EXTNF] = old[INTNF]
        new[EXIL6] = old[INIL6]

        new[DMT] = max([cont(old[EXTNF], old[DMT]), cont(old[IRP], old[DMT])])
        new[TFR1] = max(cont(old[IRP], old[TFR1]), old[SIGNAL])
        new[ZIP] = cont(old[EXTNF], old[ZIP])
        
        new[FT] = max([cont(old[EXTNF], old[FT]),cont(notfn(old[IRP]),old[FT])])
        new[BDH2] = cont(old[IRP], old[BDH2])

        new[CYTFPN] = cont(notfn(old[IRP]), old[CYTFPN])
        new[MEMFPN] = min([cont(old[CYTFPN], old[MEMFPN]), notfn(old[HEP])])

        new[IRP] = cont(notfn(old[LIP]), old[IRP])
        new[LIP] = cont(minimum([maximum([minimum([old[FE3], old[TFR1]]),minimum([old[FE2], old[DMT], old[ZIP]]), old[HO1]]),minimum([notfn(old[MEMFPN]), notfn(old[FT])])]), old[LIP])

        new[FE3] = 2
        new[FE2] = 2
        new[HEP] = cont(old[EXIL6], old[HEP])

        new[EHEME] = 2
        new[HO1] = minimum([old[EHEME], cont(old[NRF2], old[HO1])])

        if old[SIGNAL]>=1:
            new[NRF2]=2
        elif old[SIGNAL]==0:
            new[NRF2]=1
                
        self.states = new
        return new if new == old else False
        
#utils
def notfn(value):
    if(value == 0):
        return 2
    elif(value == 1):
        return 1
    elif(value == 2):
        return 0
    else:
        raise ValueError("not_ternary received a value not in [0,1,2] = " + str(value))

def cont(src, old_tgt):
    newtgt = 9 # any value assignment
    if src > old_tgt:
        newtgt = min(2, old_tgt + 1) 
    elif src == old_tgt:
        newtgt  = old_tgt
    elif src < old_tgt:
        newtgt = max(0, old_tgt - 1) 
    return newtgt

def maximum(values):
    cur_max = values[0]
    for x in values:
        cur_max = x if x > cur_max else cur_max
    return cur_max

def minimum(values):
    cur_min = values[0]
    for x in values:
        cur_min = x if x < cur_min else cur_min
    return cur_min

#Check if the current list of states is a cycle, if it is return the sub portion of the list,
# if not add cur state and return
def exists_in_list(curr_list, value):
    index = 0
    for v in curr_list:
        if value == v:
            return True, curr_list[index:]
        index += 1
    curr_list.append(value)
    return False, curr_list

#MAIN
def main(argv):
    model = Model()
    allstates = []
    attractor_states = []
    cycles_states = [] # list of steady cycles
    n = int(argv[2]) #number of sims to run
    f = open(argv[1], "w+")

    init_states = []

#####init done#################################################################################################################
    tempnodes = ['FUNGUS', 'SIGNAL','INIL6', 'INTNF', "EXIL6", 'EXTNF',"DMT", 'TFR1','ZIP','FT','BDH2', 'CYTFPN', 'MEMFPN', 'IRP', 'LIP','FE2', 'FE3', "HEP", "EHEME", "HO1", "NRF2"]

    for _ in itertools.repeat(None, n):
        temp = [0] * NUM_AGENTS
        for i in range(len(nodes)):
                temp[i] =  random.randint(0,2)
        model.set_init_states(temp)
        init_states.append(temp)
        #print init_states

        #run to see if there is a steady state
        run_num = 0
        found_steady = False
        possible_cycle = []
        possible_cycle.append(temp)
        cycle = False
        endupstate = []
        while (not(found_steady) and run_num < 500 and not cycle):
            endupstate.append(model.states)
            found_steady = model.update_states() # update list
            
            if not found_steady:
                cycle, possible_cycle = exists_in_list(possible_cycle, model.states) # chceck for cycle, add to possible if not, else return true
            run_num+= 1
        if(found_steady and not cycle):
            attractor_states.append(model.states)
            endupstate.append(model.states)
            allstates.append(endupstate)
        elif(cycle): #possible_cycle is now a confirmed steady cycle
            cycles_states.append(possible_cycle)

#####output#################################################################################################################
    #print num of unique inputs
    init_states.sort()
    unique_inits = list(init_states for init_states,_ in itertools.groupby(init_states))
    f.write("num init = " + str(n) + "\nnum unique init = " + str(len(unique_inits)) + "\n")
    f.write("num fixed = " + str(len(attractor_states)))

    print("num init = " + str(n) + "\nnum unique init = " + str(len(unique_inits)))
   #print found attractors##################################################################################################
    print("num fixed = " + str(len(attractor_states)))
    #unique attractors
    attractor_states.sort()
    unique_steady = list(attractor_states for attractor_states,_ in itertools.groupby(attractor_states))
    #print found attractors
    print("num unique fixed = " + str(len(unique_steady)))
    f.write("\nunique fixed:" + str(len(unique_steady))+ "\n")
    f.write(str(nodes) +"\n")
    
    attsteps = []
    forbasin = []
    for i in unique_steady:
        basin = []
        for j in allstates:
            if i==j[-1]:
                basin.append(j)
        steps = [len(b)-1 for b in basin]
        attsteps.append([i, [[k, steps.count(k)] for k in list(set(steps))]])

        flatbasin= [list(itertools.chain.from_iterable(basin))]
        forbasin.append(flatbasin[0])
    for i in forbasin:
        #print(dict(zip(nodes, i[-1])))
        #print(i[-1], len([list(s) for s in set(tuple(h) for h in i)]))
        f.write(str(i[-1]) + "\t" + str(len([list(s) for s in set(tuple(h) for h in i)])) + "\n")
        #print [list(s) for s in set(tuple(h) for h in i)]

    #print found cycles#########################################################################################################
    print("num cycles = " + str(len(cycles_states)))
    f.write("\nnum cycles:" + str(len(cycles_states))+ "\n")
    #unique cycles
    seen_states = {}
    unique_cycles = []
    for cycle_x in cycles_states:
        added = False
        for state_x in cycle_x:
            key = str(state_x)
            if key in seen_states:
                #do not add, not unique
                pass
            else:
                seen_states[key] = 1
                if(not added): # only add the cycle on first unseen occurance of a state
                    unique_cycles.append(cycle_x)
                    added = True

   

    print("num unique cycles = " + str(len(unique_cycles)))
    f.write("unique cycles:" + str(len(unique_cycles))+ "\n")
    for a in unique_cycles:
        f.write(str(a) + "\n")

        
    f.write("\n""\n""\nSteps (list[2,0], inputs) to reach attractor state (list item 1) from initial input.\n\n")
    for i in attsteps:
        f.write(str(i) + "\n\n")

    for i in allstates:
        f.write(str(i) + "\n\n")

if __name__ == '__main__':
    # execute only if run as a script
    main(sys.argv)

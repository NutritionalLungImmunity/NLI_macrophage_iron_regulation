#!/usr/bin/python3
import itertools
import random
import sys

LIP = 0
FT = 1
TFR1 = 2
TF = 3
FPN = 4
IRP = 5
HEP = 6
TNF = 7
DMT = 8
ZIP = 9
NTBI = 10
HP = 11
EHEME = 12
HB = 13
HPX = 14
CD163 = 15
CD91 = 16
HO1 = 17
IHEME = 18
BDH2 = 19
MTLIP = 20
NUM_AGENTS = 21

nodes = ["LIP", "FT", "TFR1", "TF", "FPN", "IRP", "HEP", "TNF", "DMT","ZIP", "NTBI", "HP", "EHEME", "HB", "HPX", "CD163", "CD91", "HO1", "IHEME", "BDH2", "MTLIP"]

class Model():
    def __init__(self):
        self.states = []
    def set_init_states(self, array_of_states):
        self.states = array_of_states
    def update_states(self):
        new = [0] * len(self.states)
        old = self.states

        new[LIP] = continuity(minimum([maximum([minimum([old[TF], old[TFR1], maximum([old[DMT], old[ZIP]])]),minimum([old[NTBI], maximum([old[DMT], old[ZIP]])]), old[HO1]]),minimum([notfn(old[FPN]), notfn(old[FT]), notfn(old[BDH2])])]), old[LIP]) 

        new[FT] = maximum([continuity(old[TNF], old[FT]), continuity(notfn(old[IRP]),old[FT])]) 
       
        new[FPN] = minimum([continuity(notfn(old[IRP]), old[FPN]), continuity(notfn(old[HEP]), old[FPN])])
        new[TFR1] = continuity(old[IRP], old[TFR1])
        new[IRP] = continuity(notfn(old[LIP]), old[IRP])
        new[TNF] = 1 
        new[HEP] = 1 
        new[TF] = 1
        new[DMT] = maximum([continuity(old[TNF], old[DMT]), continuity(old[IRP], old[DMT])])
        new[NTBI] = 1
        new[ZIP] = continuity(old[TNF], old[ZIP])
        
        new[HP] = 1
        new[EHEME] = 1
        new[HB] = 1
        new[HPX] = 1
        new[CD163] = 1
        new[CD91] = 1
        new[IHEME] = continuity(minimum([notfn(old[HO1]), maximum([minimum([old[EHEME], old[HPX], old[CD163]]), minimum([old[HB], old[HP], old[CD91]])])]), old[IHEME])
        new[HO1] = continuity(old[IHEME], old[HO1])
        new[BDH2] = minimum([continuity(old[IRP], old[BDH2]), continuity(notfn(old[TNF]), old[BDH2])])
        new[MTLIP] =  maximum([continuity(old[LIP], old[MTLIP]), continuity(old[BDH2], old[MTLIP])])

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

def continuity(src, old_tgt):
    newtgt = 9
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

#####init done#########################################################
#########################################################

    for _ in itertools.repeat(None, n):
        temp = [0] * NUM_AGENTS
        for i in range(len(nodes)):
                temp[i] =  random.randint(0,2)
        model.set_init_states(temp)
        init_states.append(temp)
        
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


#####output##################################################################
    #print num of unique inputs
    init_states.sort()
    unique_inits = list(init_states for init_states,_ in itertools.groupby(init_states))
    f.write("num init = " + str(n) + "\nnum unique init = " + str(len(unique_inits)) + "\n")
    f.write("num fixed = " + str(len(attractor_states)))

   #print found attractors ##########################################################################
    #print("num fixed = " + str(len(attractor_states)))
    print("num init = " + str(n) + "\nnum unique init = " + str(len(unique_inits)))
    #unique attractors
    attractor_states.sort()
    unique_steady = list(attractor_states for attractor_states,_ in itertools.groupby(attractor_states))
    #print found attractors
    print("num unique fixed = " + str(len(unique_steady)))
    print nodes
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
        print i[-1], len([list(s) for s in set(tuple(h) for h in i)])
        f.write(str(i[-1]) + "\t" + str(len([list(s) for s in set(tuple(h) for h in i)])) + "\n")
        #print [list(s) for s in set(tuple(h) for h in i)]

    #print found cycles###################################################################

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
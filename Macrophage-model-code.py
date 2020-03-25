import collections
from collections import OrderedDict
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import colors
import random
%matplotlib inline

mypath = [['time','BDH2', 'BDH2FE', 'CD163', 'CD91', 'CYTFPN', 'DMT', 'EHEME', "EXIL6", 'EXTNF',"FPNR", \
           'FT','FTFE','FUNGUS','HB', 'HEP', 'HO1', 'HP', 'HPX', 'IHEME', 'INIL6', 'INTNF', 'IRP',\
           'LIP', 'MEMFPN','NTBI', 'SIGNAL', 'TF', 'TFR1', 'ZIP']]

def get3ss(trydict, count):
    od =OrderedDict(sorted(trydict.items(), key=lambda t: t[0]))
    input_state = od.values()
    print od
    print len(od)
    print len(input_state)
    
    #path.append(input_state)
    mypath.append(["".join(["t"+str(count)])]+input_state)
    
    new_BDH2 =od.get('IRP') 
    
    new_BDH2FE = min([od.get('BDH2'), od.get('LIP')])
    new_CD163 = od.get("CD163")
    new_CD91 = od.get("CD91")
    
    new_DMT = max([                           \
        cont(od.get('EXTNF'), od.get('DMT')), \
        cont(od.get('IRP'), od.get('DMT'))    \
        ])
    
    new_EHEME = od.get('EHEME')
    new_EXTNF = od.get('INTNF')
    
    new_EXIL6 = od.get('INIL6')
    
    new_FPNR = od.get('FPNR')
    new_CYTFPN = min([cont(od.get("FPNR"), od.get("CYTFPN")),               \
                      cont(notfn(od.get("IRP")), od.get("CYTFPN"))])
    
    new_MEMFPN = min([cont(od.get("CYTFPN"), od.get("MEMFPN")), notfn(od.get("HEP"))]) 
      
    new_FT = max([                          \
        cont(od.get('EXTNF'), od.get("FT")),  \
        cont(notfn(od.get("IRP")),od.get("FT")) \
        ]) 
    
    new_FTFE = min([od.get('FT'), od.get("LIP")])
    
    
    new_FUNGUS = od.get('FUNGUS') 
    new_HB = od.get("HB")
    new_HEP = cont(od.get("EXIL6"), od.get("HEP"))
    new_HO1 = cont(od.get("IHEME"), od.get("HO1"))
    #new_HO1 = 1
    new_HP = od.get("HP")
    new_HPX = od.get("HPX")
    
    new_IHEME = cont(min([   \
         notfn(od.get("HO1")), \
         max([min([od.get("EHEME"), od.get("HPX"), od.get("CD163")]), min([od.get("HB"), od.get("HP"), od.get("CD91")])])]), \
            od.get("IHEME"))
       
        
    if od.get("SIGNAL")>=1:
        new_INIL6=2
    elif od.get("SIGNAL")==0:
        new_INIL6=1
        
    if od.get("SIGNAL")>=1:
        new_INTNF=2
    elif od.get("SIGNAL")==0:
        new_INTNF=2#1
        
    
    new_IRP = cont(notfn(od.get("LIP")), od.get("IRP"))
    
    ########################## LIP END ################# 
    
    new_LIP = od.get("LIP")
    
    tfin = min([od.get("TF"), od.get("TFR1"), max([od.get("DMT"), od.get("ZIP")])])
    ntbiin = min([ \
        od.get("NTBI"), \
        max([od.get("DMT"), od.get("ZIP")]) \
                 ])
    hemein = od.get("HO1")
    
    fpnin = od.get("MEMFPN")
    ftin = od.get("FT")
    bdh2in = od.get("BDH2")    
        
    posin = [tfin, ntbiin, hemein]
    negin = [fpnin, ftin, bdh2in]
    
    if max(posin) ==2 or max(negin)==2:
        if sum([i==2 for i in posin]) > sum([i==2 for i in negin]):
            new_LIP = min([od.get("LIP")+1, 2])
        elif sum([i==2 for i in posin]) < sum([i==2 for i in negin]):
            new_LIP = max([od.get("LIP")-1, 0])
        elif sum([i==2 for i in posin]) == sum([i==2 for i in negin]):
            new_LIP == od.get("LIP")
    else:
        new_LIP == od.get("LIP")
    
    ########################## LIP END ################# 
    
    new_NTBI = od.get("NTBI")
    new_SIGNAL = od.get("FUNGUS")
    new_TF = od.get("TF")
    
    new_TFR1 = max([cont(od.get("IRP"), od.get("TFR1")), od.get("SIGNAL")]) 
    new_ZIP = cont(od.get("EXTNF"), od.get("ZIP"))
    
    newd = {'BDH2':new_BDH2, 'BDH2FE':new_BDH2FE, 'CD163':new_CD163, 'CD91':new_CD91,            \
            'DMT':new_DMT, 'EHEME':new_EHEME, 'EXIL6':new_EXIL6, 'EXTNF':new_EXTNF, 'FPNR':new_FPNR, \
            'CYTFPN':new_CYTFPN, 'MEMFPN':new_MEMFPN, 'FT':new_FT,                \
             'FTFE':new_FTFE, 'FUNGUS':new_FUNGUS, 'HB':new_HB, 'HEP':new_HEP, 'HO1':new_HO1,      \
            'HP':new_HP, 'HPX':new_HPX, 'IHEME':new_IHEME, 'INIL6':new_INIL6, 'INTNF':new_INTNF,        \
             'IRP':new_IRP, 'LIP':new_LIP, 'NTBI':new_NTBI, 'SIGNAL':new_SIGNAL, \
            'TF':new_TF, 'TFR1':new_TFR1, 'ZIP':new_ZIP}
    
    
    newod = OrderedDict(sorted(newd.items(), key=lambda t:t[0]))
    ends_here = newod.values()
    print input_state
    print ends_here
    
    if input_state == ends_here:
        print ends_here, "This is the steady state"
        np = ["".join(["t",str(count)])]+ ends_here
        mypath.append(np)
    elif input_state != ends_here:
        print "reupdate fn with", ends_here
        get3ss(newod, count+1)
    
       
    

def notfn(val):         
    if val ==2:
        return 0
    elif val ==0:
        return 2
    elif val ==1:
        return 1
    else:
        return "input is other than 0 or 1"

def cont(src, old_tgt):
    newtgt = 9
    if src > old_tgt:
        newtgt = min(2, old_tgt + 1) 
    elif src == old_tgt:
        newtgt  = old_tgt
    elif src < old_tgt:
        newtgt = max(0, old_tgt - 1) 
    return newtgt


            
# change tf,ntbi,fungus here
fixedvars = {"ZIP": 2 , "DMT": 2, "FPNR": 2, "LIP":1, "TF":2, "NTBI":2, "FUNGUS":2, "EHEME":2, "HP":1, "HB":1, "CD91":1, "CD163":1, "HPX":1} 
nn = ['SIGNAL','FPNR', 'TF', 'NTBI', 'EHEME', 'FUNGUS', 'INIL6','INTNF', 'EXTNF', 'EXIL6', 'HEP', 'CYTFPN','MEMFPN', 'LIP', 'IRP', 'TFR1', 'DMT', 'ZIP', 'FT', 'FTFE', 'BDH2', 'BDH2FE', 'HP', 'HB', 'HPX', 'CD163', 'CD91', 'HO1', 'IHEME']
vv = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1,1] # give ur input for other nodes here
nv = dict(zip(nn, vv))
for k,v in nv.items():
    if k in fixedvars.keys():
        nv.update({k:fixedvars[k]})
print len(nv)
get3ss(nv, count =0)  

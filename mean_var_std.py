import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    a= [[list[0],list[1],list[2],],[list[3],list[4],list[5],],[list[6],list[7],list[8]]]

    am1= np.mean(a, axis=0)
    m1 = am1.tolist()

    am2= np.mean(a, axis=1)
    m2 = am2.tolist()

    am1= np.var(a, axis=0)
    v1 = am1.tolist()

    am2= np.var(a, axis=1)
    v2 = am2.tolist()

    am1= np.std(a, axis=0)
    s1 = am1.tolist()

    am2= np.std(a, axis=1)
    s2 = am2.tolist()

    am1= np.max(a, axis=0)
    ma1 = am1.tolist()

    am2= np.max(a, axis=1)
    ma2 = am2.tolist()

    am1= np.min(a, axis=0)
    mi1 = am1.tolist()

    am2= np.min(a, axis=1)
    mi2 = am2.tolist()

    am1= np.sum(a, axis=0)
    su1 = am1.tolist()

    am2= np.sum(a, axis=1)
    su2 = am2.tolist()

    #calculations= {'mean': [np.mean(a, axis=0), np.mean(a, axis=1),np.mean(a)], 'variance':  [np.var(a, axis=0), np.var(a, axis=1),np.var(a)], 'standard deviation':  [np.std(a, axis=0), np.std(a, axis=1),np.std(a)], 'max':  [np.max(a, axis=0), np.max(a, axis=1),np.max(a)], 'min':  [np.min(a, axis=0), np.min(a, axis=1),np.min(a)], 'sum':  [np.sum(a, axis=0), np.sum(a, axis=1),np.sum(a)]}
    calculations= {'mean': [m1,m2,np.mean(a)], 'variance':  [v1, v2,np.var(a)], 'standard deviation':  [s1, s2,np.std(a)], 'max':  [ma1, ma2,np.max(a)], 'min':  [mi1, mi2,np.min(a)], 'sum':  [su1, su2,np.sum(a)]}

    #calculations= np.array( [ 'variance:',  np.var(a, axis=0), np.var(a, axis=1),np.var(a)])
    return calculations




    return calculations

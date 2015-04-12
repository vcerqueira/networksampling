# This Python file uses the following encoding: utf-8
from random import randint,uniform
from copy import deepcopy

def read_filename(filename):
    data=[]
    with open(filename) as f:
        for line in f:
            value1,value2=line.split()
            data.append([value1,value2])
    return data

def read_links(filename, nmax):  
    f=read_filename(filename)
    n_iteration=0
    random_index=randint(0,len(f)-1) 
    v = f[random_index][0]
    sample=[] 
    sample.append(v) 
        

    while n_iteration <= 10000:  #nmax
        print n_iteration
        n_iteration+=1
        v_neighbours=[]
        w_neighbours=[]
        for i in range(len(f)):
            if f[i][0]==v:
                v_neighbours.append(f[i][1])
            elif f[i][1]==v:
                v_neighbours.append(f[i][0])
        random_index_w=randint(0,len(v_neighbours)-1)
        
        w = v_neighbours[random_index_w] 
        for j in range(len(f)):
            if f[j][0]==w:
                w_neighbours.append(f[j][1])
            elif f[j][1]==w:
                w_neighbours.append(f[j][0])

        v_degree=len(v_neighbours)             
        w_degree=len(w_neighbours)

        if uniform(0,1) <= float(v_degree)/float(w_degree):
            sample.append(w)  
            v=deepcopy(w) 
    return sample


def read_sample(filein,fileout):
    out= open(fileout,"w")
    for index in filein:
        print>>out, "%s"%index
    out.close()
        

if __name__ == "__main__":
    import sys
    filename=sys.argv[1]
    nmax=sys.argv[2]
    amostra=read_links(filename, nmax)
    amostra_final=read_sample(amostra,"amostra.txt")

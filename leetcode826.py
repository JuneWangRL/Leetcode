# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 15:15:41 2018

@author: user
"""

def answer826(dif,pro,wrk):
    
    for i in range(len(dif)):
        for j in range(i+1,len(dif)):
            if dif[i]>dif[j]:
                t=dif[i]
                dif[i]=dif[j]
                dif[j]=t
                t=pro[i]
                pro[i]=pro[j]
                pro[j]=t
    maxx=list()
    for i in range(len(wrk)):
        for j in  range(len(dif)-1,-1,-1):
            if dif[j]<=wrk[i]:
                maxx.append(max(pro[:j+1]))
                break
    return(sum(maxx))
print(answer826([2,4,6,7,10], [30,50,30,40,10], [4,5,6,7]))
               

     
            
        
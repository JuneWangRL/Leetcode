# -*- coding: utf-8 -*-
"""
Created on Sun May  6 22:38:21 2018

@author: user
"""

def answer830(s):
    index=list()
    listx=list()
    result=list()
    for x in s:
        listx.append(x)
    for i in range(len(s)-1):
        if listx[i]!=listx[i+1]:
            index.append(i)
    for j in range(len(index)-1):
        if index[j+1]-index[j]>=3:
            large=[index[j]+1,index[j+1]]
            result.append(large)
    k=0
    while k<len(listx):
        if listx[k]==listx[0]:
            k=k+1
    if k==len(listx):
        return [0,len(listx)-1]
    else:       
        return(result)

print(answer830("abbxxxxzyy"))      
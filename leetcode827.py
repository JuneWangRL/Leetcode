# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 15:46:34 2018

@author: user
"""

def answer827(I):
    for i in range(I.row):
        for j in range(I.col):
            rangex=list()
            if I[i,j]==1:
                rangex=rangex+1
                if i+1<=I.row and j+1<=I.col and i-1>0 and j-1>0:
                    if I[i+1,j]==1:
                        rangex=rangex+1
                        i=i+1
                    else:
                        I[i+1,j]==1
                    if I[i-1,j]==1:
                        rangex=rangex+1
                        i=i-1
                    else:
                        I[i-1,j]==1
                    if I[i,j+1]==1:
                        rangex=rangex+1
                        j=j+1
                    else:
                        I[i-1,j]==1
                    if I[i,j-1]==1:
                        rangex=rangex+1
                        j=j-1
                    else:
                        I[i,j-1]==1 
    return(rangex)
answer827([1,0],[0,1])    
                
                        
                    
                    
                        
                
                
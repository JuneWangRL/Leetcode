# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 15:00:28 2018
@author: user
"""
def answer825(lists):
    sumx=len(lists)*(len(lists)-1)
    print(sumx)
    sum1=0
    for lista in lists:
        for listb in lists:
            if lists.index(lista)!=lists.index(listb):
                if listb<=0.5*lista+7 or listb > lista or (listb>100 and lista<100):
                    sum1=sum1+1
    print(sum1)
    return (sumx-sum1)
print(answer825([16,16,17,18]))



                        






















# -*- coding: utf-8 -*-
"""
Created on Sun May 27 10:13:31 2018

@author: user
"""

class Solution:
    def splitIntoFibonacci(self, S):
        list_fb=list()
        for i in range(len(S)):
            lst=0
            for j in range(i):
                lst=lst+pow(10,j)*S[j]
                list_fb.append(lst)
            new_S=sum(S[j] for j in range(i,len(S)+1))
            for k in range(len(new_S)):
                lst1=0
                for h in range(k):
                    lst1=lst1+pow(10,h)*new_S[h]
                    list_fb.append(lst1)
            new_S=sum(S[j] for j in range(i+k,len(S)+1))
            sumx=list_fb[0]+list_fb[1]
            for i in range(len(new_S)):
                sumx2=sum(pow(10,j)*new_S[j] for j in range(i))
                if sumx==sumx2:
                    new_S=sum(new_S[j] for j in range(i,len(new_S)+1))
            if new_S==" ":
                return (list_fb) 
            else:
                return []
        
        
solution=Solution()
print(solution.splitIntoFibonacci["1101111"])
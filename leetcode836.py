# -*- coding: utf-8 -*-
"""
Created on Sun May 20 09:30:23 2018

@author: user
"""
'''
class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        if rec1[2]>rec1[0]:
            min1=rec1[0]
            max1=rec1[2]
        else:
            min1=rec1[2]
            max1=rec1[0]
        if rec1[1]>rec1[3]:
            min2=rec1[3]
            max2=rec1[1]
        else:
            min2=rec1[1]
            max2=rec1[3]
        if (rec2[0]>=max1 and rec2[2]>=max1) or  (rec2[0]<=min1 and rec2[2]<=min1) or (rec2[1]>=max2 and rec2[3]>=max2) or  (rec2[1]<=min2 and rec2[3]<=min2):
            return False
        else:
            return True
'''
class Solution:
    def pushDominoes(self, dominoes):
        result=[1]*len(dominoes)
        for i in range(len(dominoes)):
            result[i]=dominoes[i]
        if dominoes[1]=="L":
            result[0]="L"
        if dominoes[len(dominoes)-2]=="R":
            result[len(dominoes)-1]="R"
        for i in range(1,len(result)-1):
            '''
            if (dominoes[i-1]=="R" and dominoes[i]=="L") or (dominoes[i-1]=="L" and dominoes[i]=="."):
                result[i]="."
            elif (dominoes[i-1]=="R" and dominoes[i]=="R") or (dominoes[i-1]=="R" and dominoes[i]==".") or (dominoes[i-1]=="L" and dominoes[i]=="R"):
                result[i]="R"
            else:
                result[i]="L"
            '''
            if dominoes[i+1]=="R":
                if (dominoes[i-1]=="R" and dominoes[i]=="L") or (dominoes[i-1]=="L" and dominoes[i]=="."):
                    result[i]="."
                elif (dominoes[i-1]=="R" and dominoes[i]=="R") or (dominoes[i-1]=="R" and dominoes[i]==".") or (dominoes[i-1]=="L" and dominoes[i]=="R"):
                    result[i]="R"
                else:
                    result[i]="L"
            if dominoes[i+1]==".":
                if (dominoes[i-1]=="R" and dominoes[i]=="L") or (dominoes[i-1]=="L" and dominoes[i]=="."):
                    result[i]="."
                elif (dominoes[i-1]=="R" and dominoes[i]=="R") or (dominoes[i-1]=="R" and dominoes[i]==".") or (dominoes[i-1]=="L" and dominoes[i]=="R"):
                    result[i]="R"
                else:
                    result[i]="L"   
            if dominoes[i+1]=="L":
                if (dominoes[i-1]=="R" and dominoes[i]=="L") or (dominoes[i-1]=="L" and dominoes[i]=="."):
                    result[i]="L"
                elif (dominoes[i-1]=="R" and dominoes[i]=="R") or (dominoes[i-1]=="R" and dominoes[i]==".") or (dominoes[i-1]=="L" and dominoes[i]=="R"):
                    result[i]="."
                else:
                    result[i]="L"            
                
                
   
        strx=''
        results=strx.join(result)
        return results
                             
solution = Solution()
print (solution.pushDominoes(".L.R...LR..L.."))


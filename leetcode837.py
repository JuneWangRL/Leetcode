# -*- coding: utf-8 -*-
"""
Created on Sun May 20 22:52:30 2018

@author: user
"""

class Solution:
    def new21Game(self, N, K, W):
        result=0
        sumx=0
        if K>=W:
            for i in range(K-W,K):
                for j in range(1,W+1):
                    if i+j>=K:
                        sumx=sumx+1
                        if i+j<=N:
                            result=result+1
        else:
            for i in range(K):
                for j in range(1,W+1):
                    if i+j>=K:
                        sumx=sumx+1
                        if i+j<=N:
                            result=result+1
        pro=result/sumx        
        return(pro)
solution = Solution()
print(solution.new21Game(21, 15, 10))                
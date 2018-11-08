# -*- coding: utf-8 -*-
"""
Created on Mon May 28 20:09:57 2018

@author: user
"""

class Solution:
    def onepoint(self,i,j,col,grid):
        grid[i][j]=col
        stack=[(i,j)]
        sz=1
        while stack:
            i,j=stack.pop()
            for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni=i+di
                nj=j+dj
                if ni>=0 and nj>=0 and ni<len(grid) and nj<len(grid[0]) and grid[ni][nj]==1:
                    grid[ni][nj]=col
                    sz=sz+1
                    stack.append([ni,nj])
        return sz
    def largestIsland(self, grid):
        col=1
        mp={}
        mxsize=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    col+=1
                    mp[col]=self.onepoint(i,j,col,grid)
                    mxsize=max(mp[col],mxsize)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                newset=set([])
                if grid[i][j]==0:
                    for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                        ni=i+di
                        nj=j+dj 
                        if ni>=0 and nj>=0 and ni<len(grid) and nj<len(grid[0]) and grid[ni][nj]!=0:                    
                            newset.add(grid[ni][nj])
                newsize=1+sum(mp[s] for s in newset)
                mxsize=max(mxsize,newsize)
        return mxsize
solution=Solution()
print(solution.largestIsland([[0,1],[1,1]]))                
    
                    
                    
        



                        
                                
                            
                        
                    
                
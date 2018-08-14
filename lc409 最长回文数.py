# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 13:33:36 2018

@author: user
"""
class Solution:
	def longestPalindrome(self, s):
	   dic={}
	   for i in range(65,123):
		   dic[chr(i)]=0
	   for i in range(len(s)):
		   dic[s[i]]+=1
	   
	   result={}
	   for key,value in dic.items():
		   if value>0:
			   result[key]=value
	   num=0
	   lenth=0
	   for key,value in result.items():
		   if value%2==0:
			   lenth=lenth+value
		   if value%2==1:
			   lenth=lenth+value-1
			   num=num+1
	   if num==0:
		   return lenth
	   if num>0:
		   return lenth+1
solution=Solution()
x=solution.longestPalindrome('sdfghjsd')
			    
		   
		   
		   
		   
		   
		   
		   
		   
		   
		   
		   
		   

# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 15:32:12 2018

@author: user
"""

class Solution:
	def groupAnagrams(self, strs):
		dic={}
		for i in range(len(strs)):
			l="".join(sorted(strs[i]))
			if l in dic.keys():
				dic[l]=dic[l]+[strs[i]]
			else:
				dic[l]=[strs[i]]
		return list(dic.values())
solution=Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))  




      
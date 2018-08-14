# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 14:11:30 2018

@author: user
"""
#统计词数，字典去重
'''
string=input("input string:")
string_list=string.split(" ")
word_dict={}
for word in string_list:
    if word in word_dict:
        word_dict[word]+=1
    else:
        word_dict[word]=1
'''
class Solution:
    def wordPattern(self, pattern, str):
	    dic={}
	    string_list=pattern.split(" ")
	    flag=True
	    if len(string_list)!=len(str): 
		    flag=False
	    else:
		    for i in range(len(str)):
			    if str[i] in dic.keys():    
				    if dic[str[i]]!=string_list[i]:
					    flag=False
			    else:
				    if string_list[i] in dic.values():
					    return False
				    else:
					    dic[str[i]]=string_list[i]
	    return flag    
           
solution=Solution()
str = "abba"
pattern = "dog cat cat dog"
print(solution.wordPattern(pattern, str))
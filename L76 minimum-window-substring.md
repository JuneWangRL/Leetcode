# minimum-window-substring
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

```
class Solution:
	def minWindow(self, s, t):
		dic_t={}
		for i in range(len(t)):
			dic_t[t[i]]=dic_t.get(t[i],0)+1
		begin=0
		lenth=len(s)
		result=""
		for i in range(0,len(s)):
			flag=True
			d=True			
			while d==True:
				x=s[begin:i+1]
				dic_s={}
				for j in range(begin,i+1):
					dic_s[s[j]]=dic_s.get(s[j],0)+1
				for key in dic_t.keys():
					if (key not in dic_s.keys()) or (dic_t[key]>dic_s[key]):
						flag=False
						break
				if flag==False:
					d=False
				elif flag ==True:
					if lenth>=len(x):
						result=x
						lenth=len(x)
					begin=begin+1
		print(result)
		if s=="":
			return ""
		if s==t:
			return s
		if len(s)<len(t):
			return ""
		if len(s)==1 and len(t)==1 and s!=t:
			return "" 
		return result

solution=Solution()
S = "abc"
T = "ac"
print(solution.minWindow(S,T))  

```
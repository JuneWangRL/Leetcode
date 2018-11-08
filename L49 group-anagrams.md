# group-anagrams
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

```
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

 #如果有x这个key则value赋值为0，若有则在上面加1
dic[x]=dic.get(x,0)+1
```
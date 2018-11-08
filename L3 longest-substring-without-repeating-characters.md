# longest-substring-without-repeating-characters
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

```
class Solution:
    def lengthOfLongestSubstring(self, s):
        dic={}
        begin=0
        word=""
        result=0
        p=0
        for j in range(len(s)):
            dic[s[j]]=dic.get(s[j],0)+1
            if dic[s[j]]==1:
                word+=s[j]
                if result<len(s):
                    result=len(word)
            else:
                if result>p:
                    p=result
                while begin<j and dic[s[j]]>1:
                    dic[s[begin]]-=1
                    begin+=1
            word=""
            for i in range(begin,j+1):
                word+=s[i]
            if len(word)>p:
                p=len(word)
        if len(s)==result:
            p=len(s)
        if s==" ":
            p=1
        if s=="":
            p=0
        return(p)

```
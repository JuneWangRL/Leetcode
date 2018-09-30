Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

**Example 1:**

```
Input: ["flower","flow","flight"]
Output: "fl"
```

**Example 2:**

```
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

```python
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if "" in strs or strs==[]:
            return ""
        maxs=len(strs[0])
        for i in range(len(strs)):
            if len(strs[i])<maxs:
                maxs=len(strs[i])
        re=''
        l=[]
        for j in range(maxs):
            s=set()
            for x in strs:
                s.add(x[j])
            if len(s)==1:
                l.append(list(s)[0])
            else:
                break      
        print(l)
        return ''.join(l)
```


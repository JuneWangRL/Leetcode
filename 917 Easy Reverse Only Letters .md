Given a string `S`, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

**Example 1:**

```
Input: "ab-cd"
Output: "dc-ba"
```

**Example 2:**

```
Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
```

**Example 3:**

```
Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
```

```python
class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        r=[]
        dicx=[]
        dicy=[]
        for i in range(len(S)-1,-1,-1):
            if S[i].isalpha():
                r.append(S[i])
            else:
                dicx.append(i)
                dicy.append(S[i])
        re=[]
        print(dicx)
        print(dicy)
        print(r)
        iz=0
        for i in range(len(S)):
            if i not in dicx:
                re.append(r[iz])
                iz+=1
            else:
                re.append(dicy[dicx.index(i)])
        return "".join(re)
```

**Algorithm**

* 建立两个list分别储存字符和非字符型
* 按照条件将两个list依次排序
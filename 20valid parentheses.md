Given a string containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

**Example 1:**

```
Input: "()"
Output: true
```

**Example 2:**

```
Input: "()[]{}"
Output: true
```

**Example 3:**

```
Input: "(]"
Output: false
```

**Example 4:**

```
Input: "([)]"
Output: false
```

**Example 5:**

```
Input: "{[]}"
Output: true
```

总结：可以用抵消法则

```python
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s=='':
            return True
        if len(s)%2 != 0:
            return False
        while "[]" in s or "{}" in s or "()" in s:
            s = s.replace('[]','').replace('{}','').replace('()','')
        if s=='':
            return True
        else:
            return False
```

​        
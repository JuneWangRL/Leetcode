You are climbing a stair case. It takes *n* steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

**Note:** Given *n* will be a positive integer.

**Example 1:**

```
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```

**Example 2:**

```
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

```python
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        lst = [0] * n
        print(lst)
        lst[0]=1
        lst[1]=2
        for i in range(2,n):
            lst[i]=lst[i-1]+lst[i-2]
        return lst[n-1]
```

说明：动态规划问题，第n步的情况=第n-1步+第n-2步

1. 初始状态
2. 状态转移方程


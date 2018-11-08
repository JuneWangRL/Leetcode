Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

```
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
```

The minimum path sum from top to bottom is `11` (i.e., **2** + **3** + **5** + **1** = 11).

```python
class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for i in range(1,len(triangle)):
            for j in range(i+1):
                if j==0:
                    triangle[i][j]=triangle[i][j]+triangle[i-1][j]
                elif j==i:
                    triangle[i][j]=triangle[i][j]+triangle[i-1][j-1]
                else:
                    triangle[i][j]=min(triangle[i][j]+triangle[i-1][j-1],triangle[i][j]+triangle[i-1][j])
        return min(triangle[-1])
```

动态规划解决


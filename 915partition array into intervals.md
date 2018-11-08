### 915. Partition Array into Disjoint Intervals

Given an array `A`, partition it into two (contiguous) subarrays `left` and `right` so that:

- Every element in `left` is less than or equal to every element in `right`.
- `left` and `right` are non-empty.
- `left` has the smallest possible size.

Return the **length** of `left` after such a partitioning.  It is guaranteed that such a partitioning exists.

 

**Example 1:**

```
Input: [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]
```

**Example 2:**

```
Input: [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]
```

```python
class Solution:
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        lenth=len(A)
        maxa=[0]*lenth
        mina=[0]*lenth
        m=A[0]
        n=A[-1]
        for i in range(len(A)):
            m=max(m,A[i])
            maxa[i]=m
        for i in range(len(A)-1,-1,-1):
            n=min(n,A[i])
            mina[len(A)-i-1]=n  
        for i in range(0,len(A)-1):
            if maxa[i]<=mina[len(A)-i-2]:
                return i+1
```

用向量存储最大最小值，防止超时。
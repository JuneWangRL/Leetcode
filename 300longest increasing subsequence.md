Given an unsorted array of integers, find the length of longest increasing subsequence.

**Example:**

```
Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
```

```python
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp=[1]*(len(nums))
        for i in xrange(len(nums)):
            for j in xrange(i):
                if nums[i]>nums[j] and dp[i]<dp[j]+1:
                    dp[i]=dp[j]+1
        if len(dp)==0:
            return 0
        return max(dp)
```

动态规划 利用python2
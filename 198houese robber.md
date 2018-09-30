You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight **without alerting the police**.

**Example 1:**

```
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
```

**Example 2:**

```
Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
```

```python
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        re=[0]*len(nums)
        if len(nums)==1:
            return nums[0]
        if nums[1]>nums[0]:
            re[0]=nums[0]
            re[1]=nums[1]
        else:
            re[0]=nums[0]
            re[1]=nums[0]
        if len(nums)==2:
            return max(re[0],re[1])
        for i in range(2,len(nums)):
            re[i]=max(re[i-2]+nums[i],re[i-1])
        return re[len(nums)-1]
```

状态转移方程：第i步的最大数=max(第i-1步，第i-2步+第i家财产值)
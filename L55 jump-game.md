# Jump-game
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.
Example 1:
Input: [2,3,1,1,4]Output: trueExplanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
##### 思路：
贪心算法
```
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        location=0
        if nums[0]==0 and len(nums)==1:
            return True
        while location<len(nums)-1 and nums[location]!=0:
            jump=nums[location]
            max_jump=0
            for j in range(location+1,location+nums[location]+1):
                if j<len(nums) and nums[j]+j>max_jump:
                    max_jump=nums[j]+j
                    jump=j
            location=jump
            print(location)
        if location==len(nums)-1:
            return True
        if nums[location]==0:
            return False
        return True
```
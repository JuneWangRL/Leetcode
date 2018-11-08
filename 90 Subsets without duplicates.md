Given a collection of integers that might contain duplicates, **nums**, return all possible subsets (the power set).

**Note:** The solution set must not contain duplicate subsets.

**Example:**

```
Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
```

```python
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = []
        nums=sorted(nums)
        self.huisu(nums, [], l, 0)
        re=[]
        for x in l:
            if x not in re:
                re.append(x)
        return re
            

    def huisu(self, nums, item, l, num):
        if num >= len(nums):
            l.append(item)
            return
        item1 = item.copy()
        item2 = item.copy()
        item1.append(nums[num])
        self.huisu(nums, item1, l, num + 1)
        self.huisu(nums, item2, l, num + 1)
```


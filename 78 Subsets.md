Given a set of **distinct** integers, *nums*, return all possible subsets (the power set).

**Note:** The solution set must not contain duplicate subsets.

**Example:**

```
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
```

```python
class Solution:

    def subsets(self, nums):
        l = []
        self.huisu(nums, [], l, 0)
        return l

    def huisu(self, nums, item, l, num):
        if num >= len(nums):
            l.append(item.copy())
            return
        item1 = item.copy()
        item2 = item.copy()
        item1.append(nums[num])
        self.huisu(nums, item1, l, num + 1)
        self.huisu(nums, item2, l, num + 1)
```


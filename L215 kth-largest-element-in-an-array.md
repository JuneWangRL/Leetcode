# kth-largest-element-in-an-array
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
##### 说明：
堆排序
```
#求取顺序的时候可以用到堆排序
# python中堆的语法如下：
heapq.heapify(x) 将x变成最小堆的结构
heapq.nlargest(k,nums)  返回由nums中最大的k个值组成的堆
heapq.nsmallest(k,nums)  返回由nums中最小的k个值组成的堆
heapq.heappush(n,x) 向堆n中添加元素x
heapq.heappop(n) 弹·出堆n中顶部元素
heapq.heappushpop(n,x) 向堆n中添加元素x并弹出堆中最小元素
heapq.heapreplace(n,x) 堆n弹出最小元素再插入x元素
heapq._heapify_max(n) 将堆n变为最小堆
heapq._heappop_max(n) 返回堆中最大元素

import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        x=heapq.nlargest(k,nums)
        return heapq.nsmallest(1,x)[0]
```
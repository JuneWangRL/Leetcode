Given a linked list, return the node where the cycle begins. If there is no cycle, return `null`.

**Note:** Do not modify the linked list.

**Follow up**:
Can you solve it without using extra space?

####算法思路

* 先判断是否有环，利用第一问的方法，建立快慢指针
* 在利用set的方法找到地址相同的

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    checkSet = set()
    def hascycle(self,head):
        meet=head
        ###这里要判断的是meet.next不能是空，否则就不能跳到下一个
        while head and meet and meet.next:
            head=head.next
            meet=meet.next.next
            if meet==head:
                return True
        return False
            
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if self.hascycle(head)==False:
            return None
        else:
            while True:
                if head not in self.checkSet:
                    self.checkSet.add(head)
                else:
                    return head
                head=head.next
```


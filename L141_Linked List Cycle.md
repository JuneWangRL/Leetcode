Given a linked list, determine if it has a cycle in it.

Follow up:

Can you solve it without using extra space?

###判断链表是否有环？

####算法思路

建立快慢指针，快指针的速度是慢指针的两倍，相遇的节点为指针头节点，因此若为环 总能相遇

利用while循环，跳出循环的条件为 指针f为空，或者l为空，或者f.next为空

快慢指针从同一节点出发

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        l,f=head,head.next
        while l!=None and f!=None and f.next!=None:
            if l==f:
                return True
            l=l.next
            f=f.next.next
        return False
```

```python 
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        l,f=head,head
        while l and f and f.next:
            l=l.next
            f=f.next.next
            if l==f:
                return True
        return False
```


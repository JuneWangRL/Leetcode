Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists: 

```
A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
```

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        setA=set()
        setB=set()
        while headA!=None:
            setA.add(headA)
            headA=headA.next
        while headB!=None:
            if headB in setA:
                return headB
            headB=headB.next
        return None
```


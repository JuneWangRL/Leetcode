Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

**Example:**

```
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
```

```python
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1==None:
            return l2
        if l2==None:
            return l1
        head=ListNode(0)
        res=head
        while l1!=None and l2!=None:
            if l1.val>=l2.val:
                res.next=l2
                l2=l2.next
            else:
                res.next=l1
                l1=l1.next
            res=res.next
        if l1!=None:
            res.next=l1
        else:
            res.next=l2
        return head.next  #一般都要返回链表头节点
```


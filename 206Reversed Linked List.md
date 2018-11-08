Reverse a singly linked list.

**Example:**

```
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
```

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        head_cur=head
        new_head=None
        while head_cur:
            next_node=head_cur.next #记录下一个节点
            head_cur.next=new_head #下一个节点指向new_head
            new_head=head_cur#给new_head赋值
            head_cur=next_node#重新定义head_cur     
        return new_head
            
```


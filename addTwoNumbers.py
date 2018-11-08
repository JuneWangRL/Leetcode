# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 21:14:37 2018

@author: user
"""

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_str = ""
        l2_str = ""
        while l1 :
            l1_str += str(l1.val)
            l1 = l1.next
            
        while l2:
            l2_str += str(l2.val)
            l2 = l2.next
        return [int(x) for x in str(int(l1_str[::-1]) + int(l2_str[::-1]))][::-1]
l1=2->4->3
l2=5->6->4
solution=Solution()
print(solution.addTwoNumbers(l1,l2))
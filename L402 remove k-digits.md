# Remove K-digits
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.
Note:
	• The length of num is less than 10002 and will be ≥ k.
	• The given num does not contain any leading zero.
Example 1:
Input: num = "1432219", k = 3Output: "1219"Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
思路：
利用栈解决。贪心
若k>栈顶，push进入；
若k<栈顶，弹栈，直到栈空或者不能弹出。
若最终栈内元素多于规定元素；去除最后的#位
若遇到0，不在首位的话，都保留。

```
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k<=0:return num
        if k>=len(num):return '0'
        stack=[]
        for i in range(len(num)):
            while k>0 and stack and num[i]<stack[-1]:
                stack.pop()
                k=k-1
            stack.append(num[i])
        while k>0:
            stack.pop()
            k=k-1 
        return ''.join(stack).lstrip('0') or '0'

#lstrip:去掉开头0的数字
```
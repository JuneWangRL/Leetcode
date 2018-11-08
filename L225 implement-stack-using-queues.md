# implement-stack-using-queues
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Example:

MyStack stack = new MyStack();

stack.push(1);
stack.push(2);  
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
Notes:

You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
##### 思路：
stack就是当成一个list形式的东西
给stack增加元素：stack.append() 
stack弹出元素，返回被弹出的元素：stack.pop()
stack返回栈顶元素，注意：stack从下面开始从0计算，stack[len(self.stack)-1]
判断是否是empty stack==[]
队列是先进先出的线性表
```
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack=[]    

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.stack.append(x)    

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.stack.pop()
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.stack[len(self.stack)-1]
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.stack==[]

```

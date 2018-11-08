### 919. Complete Binary Tree Inserter

A *complete* binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.

Write a data structure `CBTInserter` that is initialized with a complete binary tree and supports the following operations:

- `CBTInserter(TreeNode root)` initializes the data structure on a given tree with head node `root`;
- `CBTInserter.insert(int v)` will insert a `TreeNode` into the tree with value `node.val = v` so that the tree remains complete, **and returns the value of the parent of the inserted TreeNode**;
- `CBTInserter.get_root()` will return the head node of the tree.

**Example 1:**

```
Input: inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]]
Output: [null,1,[1,2]]
```

**Example 2:**

```
Input: inputs = ["CBTInserter","insert","insert","get_root"], inputs = [[[1,2,3,4,5,6]],[7],[8],[]]
Output: [null,3,4,[1,2,3,4,5,6,7,8]]
```

 

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class CBTInserter(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.nodes=[]
        q=[root]
        while q:
            self.nodes.extend(q)
            q=[c for n in q for c in n.left,n.right if c]
                        
    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        i=len(self.nodes)
        self.nodes.append(TreeNode(v))
        j=(i-1)//2
        if i%2:
            self.nodes[j].left=self.nodes[i]
        else:
            self.nodes[j].right=self.nodes[i]
        return self.nodes[j].val
       
    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.nodes[0]
        
```

**分析**

* 二叉树从左到右依次填满，只有每一层的最后一个可能会不是满的。

**算法思路**

* 层次遍历，每一层的节点按照从左到右的顺序依次push进入list
* 计算list的长度，如果lenth%2==0，将元素push进入（lenth-1）/2的左边，否则push进入右边。（通过画图可以知道）
* 树形结构多种多样，最好先画图理解细节。
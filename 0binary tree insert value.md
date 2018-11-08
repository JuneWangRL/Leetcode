```python
#递归实现insert
class Treenode(object):
    def __init__(self,x):
        self.left=None
        self.right=None
        self.value=x
        
def bst_insert(node,insertnode):
    if insertnode>node.value:
        if node.left:
            bst_insert(node.left,insertnode)
        else:
            node.left=Treenode(insertnode)
    else:
        if node.right:
            bst_insert(node.right,insertnode)
        else:
            node.right=Treenode(insertnode)
node=Treenode(10)
bst_insert(node,5)
bst_insert(node,11)
```

```python
#while循环在二叉树中插入value
def while_insert(node,insertnode):
    while node.value!=insertnode:
        if node.value<insertnode:
            if node.right:
                node=node.right
            else:
                node.right=Treenode(insertnode)
        else:
            if node.left:
                node=node.left
            else:
                node.left=Treenode(insertnode)
```

```python
#二叉树先序遍历得到的是一个list从大到小的排列
def front_digui(root):
    """利用递归实现树的先序遍历"""
    if root == None:
        return
    print(root.value)
    front_digui(root.left)
    front_digui(root.right)
```

意味着如果想要排序，也可以用二叉查找树的方式先建立树，再先序遍历。

```python
#二叉查找树，找到相应的value值
def binary_search(node,val):
    while node:
        if node.value==val:
            return True
        if val<node.value:
            node=node.left
        else:
            node=node.right
    return False
```


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





There are a total of *n* courses you have to take, labeled from `0` to `n-1`.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: `[0,1]`

Given the total number of courses and a list of prerequisite **pairs**, is it possible for you to finish all courses?

**Example 1:**

```
Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
```

**Example 2:**

```
Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
```

```python
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        
        Time: O(N)
        Space: O(N) on stack frame. O(N) on heap.
        """
        graph = defaultdict(list)
        visited = {}
        for child,parent in prerequisites:
            graph[parent].append(child)
        #双重循环，对于每一个course都进行一次宽度遍历
        for course in range(numCourses):
            if not self.visit(graph,visited,course):
                return False
        return True
        
    def visit(self, graph, visited, node):
        if visited.get(node) == 'P': #Seen in a previous iteration, 'Permanently Marked'
            return True
        if visited.get(node) == 'T': #Seen in the same iteration of DFS, 'Temporaily Marked'
            return False
        visited[node] = 'T'
        for child in graph.get(node,[]):
            if not self.visit(graph,visited,child):
                return False
        visited[node] = 'P'
        return True
```

### Depth-first search[[edit](https://en.wikipedia.org/w/index.php?title=Topological_sorting&action=edit&section=4)]

An alternative algorithm for topological sorting is based on [depth-first search](https://en.wikipedia.org/wiki/Depth-first_search). The algorithm loops through each node of the graph, in an arbitrary order, initiating a depth-first search that terminates when it hits any node that has already been visited since the beginning of the topological sort or the node has no outgoing edges (i.e. a leaf node):

```
L ← Empty list that will contain the sorted nodes
while there are unmarked nodes do
    select an unmarked node n
    visit(n) 
```



```
 function visit(node n)
    if n has a permanent mark then return
    if n has a temporary mark then stop   (not a DAG)
    mark n temporarily
    for each node m with an edge from n to m do
        visit(m)
    mark n permanently
    add n to head of L
```

Each node *n* gets *prepended* to the output list L only after considering all other nodes which depend on *n* (all descendants of *n* in the graph). Specifically, when the algorithm adds node *n*, we are guaranteed that all nodes which depend on *n* are already in the output list L: they were added to L either by the recursive call to visit() which ended before the call to visit *n*, or by a call to visit() which started even before the call to visit *n*. Since each edge and node is visited once, the algorithm runs in linear time. This depth-first-search-based algorithm is the one described by [Cormen et al. (2001)](https://en.wikipedia.org/wiki/Topological_sorting#CITEREFCormenLeisersonRivestStein2001); it seems to have been first described in print by [Tarjan (1976)](https://en.wikipedia.org/wiki/Topological_sorting#CITEREFTarjan1976).
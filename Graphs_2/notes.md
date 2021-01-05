# Graphs

## Objective 01 - Describe a depth first search and its uses, and can manually run a DFS on a graph

Another method is **depth-first search** (DFS). This searching algorithm "dive down" the graph before backtracking and exploring another branch.
- Does not visit a previously explored vert

![DFS](Graphs_Notes/Graphs_1/images/dfs.png)

### **Applications of DFS**

DFS is often the preferred method or exploring a graph if we want to ensure we visit every node in the graph. As an example, let's say that we have a graph that represents all the friendships in the entire world. We want to find a path between two known people Andy and Sarah. If we used a depth-first search in this scenario we could end up extremely far away from Andy while still not finding a path to Sarah. Using a DFS, we will eventually find the path, but it won't find the shortest path and it will also likely take a long time.

So, this is an example of where a DFS would not work well. What about a good use case for DFS. Here are a few examples:

* Finding Minimum Spanning Trees (Links to an external site.) of weighted graphs
* Path finding
* Detecting cycles in graphs
* Topological sorting (Links to an external site.), useful for scheduling sequences of dependent jobs
* Solving and generating mazes

**Coloring Vertices**
Useful to color verts as we arrive at them and as we leave them behind as "already searched".

**Recursion**
Since DFS wil pursue leads in the graph as far as it can, and then "back up", recursion is a good approach to remember where we left of.

```
explore(graph) {
    visit(this_vert);
    explore(remaining_graph);
}
```

**Psuedo-code for DFS**
```
DFS(graph):
    for v of graph.verts:
        v.color = white
        v.parent = null

    for v of graph.verts:
        if v.color == white:
            DFS_visit(v)

DFS_visit(v):
    v.color = gray

    for neighbor of v.adjacent_nodes:
        if neighbor.color == white:
            neighbor.parent = v
            DFS_visit(neighbor)

    v.color = black
```

## **Example**

```
class Graph:
    def __init__(self):
        self.vertices = {
                            "A": {"B", "C", "D"},
                            "B": {},
                            "C": {"E", "F"},
                            "D": {"G"},
                            "E": {"G"},
                            "F": {"J"},
                            "G": {},
                            "H": {"C", "J", "K"},
                            "I": {"D", "E", "H"},
                            "J": {"L"},
                            "K": {"C"},
                            "L": {"M"},
                            "M": {},
                            "N": {"H", "K", "M"}
                        }
```
On your own, complete the following tasks:

* Spend a few minutes researching to find a unique use-case of a breadth-first-search that we did not mention in the list above.

* Using the graph represented below, draw a picture of the graph and label each of the verts to show the correct vertex visitation order for a depth-first-search starting with vertex "I".

One method we can use when searching a graph is **breadth first search(BFS)**. This sorting algorithm explores the graph outward in rings of increasing distance from teh starting vertex. The algorithm never attempts to explore a vert it has already explored or is currently exploring.

When starting from teh upper left, the numbers on this graph show a vertex vistitation order in a BFS:

![BFS](Graphs_Notes/Graphs_1/images/bfs.png)

*Note: it's important to know the distinction between a breadth-first search and traversal. A BFT is when you visit each vertex in breadth first order and do something during the traversal. A breadth-first search is when you search through vertexes in breadth-first order until you find the target vertex. A breadth-first search usually returns the shortest path from the starting vertex to the target vertex once the target is found.*

### **Applications of BFS**

* Pathfinding, Routing
* Find neighbor nodes in a P2P network like BitTorrent
* Web crawlers
* Finding people n connections away on a social network
* Find neighboring locations on graph
* Broadcasting in a network
* Cycle detection in a graph
* Finding Connected Components (Links to an external site.)
* Solving several theoretical graph problems

**Coloring Vertexes**
Useful to color verts as we arrive at them and as we leave them behind as "already searched".

**Keeping Track of What We Need to Explore**
In a BFS, it's useful to track which nodes we need to follow up on. We can track by adding neighbors to a queue(FIFO), and then explore the verts in the queue one by one.

**Psuedo-code for BFS**
```
BFS(graph, startVert):
    for v of graph.vertexes:
        v.color = white

    startVert.color = gray
        queue.enqueue(startVert)

    while !queue.isEmpty():
        u = queue[0]  // Peek at head of the queue, but do not dequeue!

        for v of u.neighbors:
            if v.color == white:
                v.color = gray
                queue.enqueue(v)

        queue.dequeue()
        u.color = black
```

### **Challenge**

```
class Graph:
    def __init__(self):
        self.vertices = {
                            "A": {"B", "C", "D"},
                            "B": {},
                            "C": {"E", "F"},
                            "D": {"G"},
                            "E": {"G"},
                            "F": {"J"},
                            "G": {},
                            "H": {"C", "J", "K"},
                            "I": {"D", "E", "H"},
                            "J": {"L"},
                            "K": {"C"},
                            "L": {"M"},
                            "M": {},
                            "N": {"H", "K", "M"}
                        }
```

On your own, complete the following tasks:

1. Spend a few minutes researching to find a unique use-case of a breadth-first-search that we did not mention in the list above.

2. Using the graph represented below, draw a picture of the graph and label each of the verts to show the correct vertex visitation order for a breadth-first-search starting with vertex "I".

3. Besides marking verts with colors as in the pseudo-code example above, how else could you track the verts we have already visited?


How to solve any graph problem?
1. translate problem into graph (Find relationship (link up words that only are one letter off))
2. Build graph --> adjacency list
3. Traverse graph

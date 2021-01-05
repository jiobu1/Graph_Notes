# Graphs
## **Objective 01 - Describe what a graph is, explain its components, provide examples of its useful applications, and draw each of the different graph types**

- [] describe what graphs are
- [] describe their componenets
- [] what they're useful for
- [] draw graphs of different types

### **What is a graph?**
are collections of data represented by nodes and connections between nodes
- broad term, i.e. Treees

### **Parts**

* <ins>nodes or vertices</ins> -  represents objects in a data set(cities, animals, web pages)

* <ins>edges</ins> - connections between vertices; can be bidirectional
```
      edges
    O-------O
vertex     vertex
```
* <ins>unidirectional</ins> - One directional path, i.e. A --> B

* <ins>bidirectional</ins> - Edges goes back and forth, i.e. A<---->B

* <ins>weights</ins> - cost to travel across an edge (values associated with each edge)

### **Example:**
![Graph](Graphs_Notes/Graphs_1/graphs.png)
```
V = {V0, V1, V2, V3, V4, V5}
E = {(v0, v1, 5), (v1, v2, 4),
     (v2, v3, 9), (v3, v4, 7),
     (v4, v0, 1), (v0, v5, 2),
     (v5, v4, 8), (v3, v5, 3),
     (v5, v2, 1)}
```

###  **Useful for ...**
**Train Map**\
![Train Map](Graphs_Notes/Graphs_1//imagestrain_map.png)
- different stops using different nodes
- trains are the edges
- weight - length of time
- use graph to calculate quickest distance

**Network Activity** \
![Github](Graphs_Notes/Graphs_1/images/github.png)
- used graph to represent pull/ push history

**Social network**\
![Social Network](Graphs_Notes/Graphs_1//imagessocial.png)\
social networks
vertex: person
edge: friend/follower

### **Types of Graphs**
**Graph Level**
![Directed Graph](Graphs_Notes/Graphs_1/images/directed.png)\
<ins>directed graph</ins> - can only move in one direction along edges

![Undirected Graph](Graphs_Notes/Graphs_1/images/undirected.png)\
<ins>undirected graph</ins> - allows movement in both directions along edges

**Directed Graph**
![Cyclic Graph](Graphs_Notes/Graphs_1/images/cyclic.png)\
<ins>cyclic graph</ins> - edges allow you to revisit at least one vert (can go back to itself - only one node)

![Acylic Graph](Graphs_Notes/Graphs_1/images/acyclic.png)\
<ins>acyclic graph</ins> - vertices can only be visited once (no path back to itself)

<ins>dense/sparse graph</ins> - a graph where most vertices are connected to each other is considered dense. A graph with less connections is sparse. There is not exact cutoff for this but you could say a flight map is more dense than a subway map. example (**disjoined graph** - no edges)
![Flight Map](Graphs_Notes/Graphs_1/images/flight.png)
![Subway Map](Graphs_Notes/Graphs_1/images/subway.png)

<ins>weighted graphs</ins> - graphs with values (weights) associated with the edges are called *weighted graphs*
The meaning of the weight is depedent on the type of graph. (as long as one edge has a weight it's considered a weighted graph)
i.e Choosing a  route. The longer route might have a higher weight over a shorter route

<ins>unidirectional vs bidiretional edge</ins> - Only goes in one direction vs a direction that goes back and forth (edge level)

**Summary**\
Graphs are a set of vertices and edges taht connect those vertices.
Can use graphs to represent a variety of different networks or related pieces of data

## **Objective 02 - Represent a graph as an adjacency list and an adjacency matrix and compare and contrast the respective representations**

### **Graph Representations**

Two common ways to represet graphs in code ar **adjacency lists** and **adjacency matrixes**.

![Matrices vs Lists](Graphs_Notes/Graphs_1/images/adjacency_matrix_list.png)

### **Adjacency List**

In an adjacency list, the graph stores a list of vertices. For each vertex, it stores a list of each connected vertex.

![Adjacency List](Graphs_Notes/Graphs_1/images/adjacencylist.png)

Python Code:
```
class Graph:
    def __init__(self):
        self.vertices = {
                            "A": {"B"},
                            "B": {"C", "D"},
                            "C": {"E"},
                            "D": {"F", "G"},
                            "E": {"C"},
                            "F": {"C"},
                            "G": {"A", "F"}
                        }
```
The `vertice`s collection is a `dictionary` which lets us access each collection of edges in O(1) constant time. Because the edges are contained in a `set` we can check for the existence of edges in O(1) constant time

### **Adjacency Matrix**
![Adjacency List](Graphs_Notes/Graphs_1/images/adjacencylist.png)

Python code
```
class Graph:
    def __init__(self):
        self.edges = [[0,1,0,0,0,0,0],
                      [0,0,1,1,0,0,0],
                      [0,0,0,0,1,0,0],
                      [0,0,0,0,0,1,1],
                      [0,0,1,0,0,0,0],
                      [0,0,1,0,0,0,0],
                      [1,0,0,0,0,1,0]]
```

This matrix is represented as a two-dimensional array - a list of lists. With this implementation, we get the benefit of built-in edge weights. `0` denotes not relationship, but any other value that is present represents an edge label or edge weight. The drawback is that we do not have a built-in association between the vertex and their index.

In practice, implementing both the adjacency list and adjacency matrix would contain more information by including `Vertex` and `Edge` classes.

### **Tradeoffs**

Adjacency matrices and adjacency lists have strengths and weaknesses.

## **Space Complexity**

### **Adjacency Matrix**

**Complexity: `O(V^2)` space**

Consider a dense graph where each vertex points to each other vertex. Here, the total number of edges will approach V^2. This means that regardless of whether you choose an adjacency list or an adjancency matrix, both will have a comparable space complexity. However, dictionaries and sets are less space efficient than lists. So, for dense graphs (graphs with a high average number of edges per vertex), the adjacency matrix is more efficient because it uses lists instead of dictionaries and sets.

### **Adjacency List**

**Complexity: `O(V + E)` space**

Consider a sparse graph with 100 vertices and only one edge. An adjacency list would have to store all 100 vertices but only needs to keep track of that single edge. The adjacency matrix would need to store 100x100=10,000 connections, even though all but one would be 0.

*Takeaway: The worst case storage of an adjacency lists occurs when the graph is dense. In this case, the matrix and list representation have the same complexity`(O(V^2))`. However, for the general case, the list representation is usually more desirable. Also, since finding a vertex's neighbors is a common task, and adjacency lists make this operation easier, adjacency list are more often used to represent graphs.*

## **Add Vertex**

### **Adjacency Matrix**

**Complexity: `O(V)` time**

For an adjacency matrix, we would need to add a new value to the end of each existing row, then add a new row at the end.

```
for v in self.edges:
    self.edges[v].append(0)
v.append([0] * len(self.edges + 1))
```

Python lists, appending to the end of a list is `O(1)` because of over-allocation of memory but can be `O(n)` when the over-allocated memory fills up. When this occurs, adding the vertex can be `O(V^2)`.

### **Adjacency List**

**Complexity: `O(1)` time**

Adding a vertex is simple in an adjacency list:
```
self.vertices["H"] = set()
```

Adding a new key to a dictionary is a constant-time operation.

*Takeaway: Adding vertices is very inefficient for adjacency matrices but very efficient for adjacency lists.*

## **Remove Vertex**

### **Adjacency Matrix**

**Complexity: `O(V^2)` time**

Removing vertices is inefficient in both representations. In an adjacency matrix, we need to remove the removed vertex's row, then remove that column from each other row. Removing an element from a list requires moving everything after that element over by one slot which takes an average of V/2 operations. Since we need to do that for every single row in our matrix, that results in a V^2 time complexity. We need to reduce the index of each vertex after our removed by index 1 as well which doesn't add to our quadratic time complexity, but adds extra operations.

### **Adjacency List**

**Complexity: `O(V)` time**

For an adjacency list, we need to visit each vertex and remove all edges pointing to our removed vertex. Removing elements from sets and dictionaries is a O(1) operation, so this results in an overall O(V) time complexity.

*Takeaway: Removing vertices is inefficient in both adjacency matrices and lists but mroe efficient in lists.*

## **Add Edge**

### **Adjacency Matrix**

**Complexity: `O(1)`**

Adding an edge in an adjacency matrix is simple:

```
self.edges[v1][v2] = 1
```

### **Adjacency List**

**Complexity: `O(1)`**

Adding an edge in an adjacency list is simple:
```
self.vertices[v1].add(v2)
```

Both are constant time operations.

*Takeaway: Adding edges to both adjacency matrices and lists is very efficient*

## **Remove Edge**

### **Adjacency Matrix**

**Complexity: `O(1)`**

Removing an edge in an adjacency matrix is simple:

```
self.edges[v1][v2] = 0
```

### **Adjacency List**

**Complexity: `O(1)`**

Removing an edge in an adjacency list is simple:

```
self.vertices[v1].remove(v2)
```

Both are constant time operations.

*Takeaway: Removing edges to both adjacency matrices and lists is very efficient*

## **Find Edge**

### **Adjacency Matrix**

**Complexity: `O(1)`**

Finding an edge in an adjacency matrix is simple:

```
return self.edges[v1][v2] > 0
```

### **Adjacency List**

**Complexity: `O(1)`**

Finding an edge in an adjacency list is simple:

```
return v2 in self.vertices[v1]
```

Both are constant time operations.

*Takeaway: Finding edges to both adjacency matrices and lists is very efficient*

## **Get All Edges from Vertex**

### **Adjacency Matrix**

**Complexity: `O(V)`**

In an adjacency matrix, this is complicated. You would iterate through the entire row and populate a list based on teh results:

```
v_edges = []
for v2 in self.edges[v]:
    if self.edges[v][v2] > 0
        v_edges.append(v2)
return v_edges
```

### **Adjacency List**

**Complexity: `O(1)`**

With an adjacency list, this is simple as returning the value from the vertex dictionary:

```
return self.vertex[v]
```

*Takeaway: Fetching all edges is less efficient in an adjacency matrix than an adjacency list*


**Summary**\

|             | Space       | Add Vert    | Remove Vert | Add Edge    | Remove Edge | Find Edge   | Get All Edges |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | -----------   |
| Matrix      | `O(V^2)`    | `O(V)`      | `O(V^2)`    | `O(1)`      | `O(1)`      |  `O(1)`     | `O(V)`        |
| List        | `O(V+E)`    | `O(1)`      | `O(V)`      | `O(V)`      | `O(1)`      |  `O(1)`     | `O(1)`        |


In most practical use-cases, an adjacency list will be a better choice for representing a graph. But there are some dense graphs or weighted graphs that could have better space efficiency when represented by a matrix.


## **Example:**
![Adjacency Example](Graphs_Notes/Graphs_1/images/adjacency_example.png)

### **Adjacency List**
```
class Graph:
    def __init__(self):
        self.vertices = {
                            "A": {"B": 1},
                            "B": {"C": 3, "D": 2},
                            "C": {},
                            "D": {},
                            "E": {"D": 1}
                        }
}
```

The difference between this implementation and the previous adjacency list that we used is that this represenation allows our edges to have weights. 

### **Adjacency Matrix**
```
class Graph:
    def __init__(self):
        self.edges = [[0,1,0,0,0],
                      [0,0,3,2,0],
                      [0,0,0,0,0],
                      [0,0,0,0,0],
                      [0,0,0,1,0]]
```

## **Challenge Question*
![Challenge Question](Graphs_Notes/Graphs_1/images/challenge.png)

1. Using the graph shown in the picture above, write python code to represent the graph in an adjacency list.
2. Using the same graph you used for the first exercise, write python code to represent the graph in an adjacency matrix.
3. Write a paragraph that compares and contrasts the efficiency of your different representations.


## **Objective 03 - Represent a breadth-first-search of a graph in pseudo-code and recall common applications for its use**

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

### **Objective 04 - Represent a depth-first-search of a graph in pseudo-code and recall common applications for its use**

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



[1] <---- [2]
    ---->

- add vertex(1)
- add vertex(2)
- add edge (1,2)
- add edge (2,1)


Difference between traversing and searching. Stop when you find something.
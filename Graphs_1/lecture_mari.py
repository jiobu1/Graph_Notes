from collections import deque

# graph ql

class Graph:

    def __init__(self):
        # vertex_id --> set
        self.vertices = {}

    def __repr__(self):
        return str(self.vertices)

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set() # use hash table under the hood

    # Remove vertex from graph and any incoming edges to it.
    def remove_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            print("Attenmpting to remove non-existent vertex")
            return
        self.vertices.pop(vertex_id)
        for remaining_vertex in self.vertices:
            self.vertices[remaining_vertex].discard(vertex_id)

    def remove_edge(self, from_vertex_id, to_vertex_id):
        if from_vertex_id not in self.vertices or to_vertex_id not in self.vertices:
            print("Attenmpting to remove non-existent edge")
            return
        self.vertices[from_vertex_id].discard(to_vertex_id)

    #Adds a directed edge from_vertex_id to to_vertex_id
    def add_edge(self, from_vertex_id, to_vertex_id):
        if from_vertex_id not in self.vertices or to_vertex_id not in self.vertices:
            print("Attempting to add edge to non-existing nodes")
            return
        self.vertices[from_vertex_id].add(to_vertex_id)

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        visited = set()
        queue = deque()
        queue.append(starting_vertex)
        while len(queue) > 0:
            currNode = queue.popleft()
            if currNode not in visited:
                visited.add(currNode)
                print(currNode)
                for neighbor in self.vertices[currNode]:
                    queue.append(neighbor)

    # returns a path to the goal_vertex and from starting_vertex
    def bfs(self, starting_vertex, goal_vertex):
        visited = set()
        queue = deque()
        # Push current path you're on onto the stack instead of just a single vertex
        queue.append([starting_vertex])
        while len(queue) > 0:
            currPath = queue.popleft()
            currNode = currPath[-1] # the current node you're on is the last node in the path
            if currNode == goal_vertex:
                return currPath
            if currNode not in visited:
                visited.add(currNode)
                for neighbor in self.vertices[currNode]:
                    newPath = list(currPath)
                    newPath.append(neighbor)
                    queue.append(newPath)

    def dft(self, starting_vertex):
        visited = set()
        stack = deque()
        stack.append(starting_vertex)
        while len(stack) > 0:
            currNode = stack.pop()
            if currNode not in visited:
                visited.add(currNode)
                print(currNode)
                for neighbor in self.vertices[currNode]:
                    stack.append(neighbor)

    # returns a path to the goal_vertex and from starting_vertex
    def dfs(self, starting_vertex, goal_vertex):
        visited = set()
        stack = deque()
        # Push current path you're on onto the stack instead of just a single vertex
        stack.append([starting_vertex])
        while len(stack) > 0:
            currPath = stack.pop()
            currNode = currPath[-1] # the current node you're on is the last node in the path
            if currNode == goal_vertex:
                return currPath
            if currNode not in visited:
                visited.add(currNode)
                for neighbor in self.vertices[currNode]:
                    newPath = list(currPath)
                    newPath.append(neighbor)
                    stack.append(newPath)




##################################################################################################################################################
graph = Graph()
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
print(graph)

graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 4)
graph.add_edge(4, 1)

print(graph)

# print(graph.get_neighbors(1)) # 2, 3
# print(graph.get_neighbors(4)) # 1

# graph.remove_vertex(4)
# graph.remove_vertex(1)

# graph.remove_edge(2, 4)
graph.bft(4)

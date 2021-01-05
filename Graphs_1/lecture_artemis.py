# Graphs
https://www.programiz.com/dsa/graph-bfs
"""
Simple graph implementation
"""

from util import Stack, Queue

class Graph:
    """ Represent a graph as a dictionary of vertice mapping labels to edges"""
    def __init__(self):
        self.vertices = {} # space O(V)+O(E)

    def add_vertex(self, vertex_id): # O(1)
        """
        Add a vertex to the graph
        """
        # Create the new key with the vertex_id, and set the value to an empty set
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2): # O(1)
        """
        Add a directed edge to the graph
        """
        # Find vertex V1 in our vertices, add V2 to the set of edges
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def bidirected_edge(self, v1, v2):
        self.add_edge(v1, v2)
        self.add_edge(v2, v1)

    def remove_edge(self, v1, v2): # O(V) make sure there are edges that don't make sense.
        """
        Add a directed edge to the graph
        """
        # Find vertex V1 in our vertices, add V2 to the set of edges
        pass

    def get_neighbors(self, vertex_id): # O(1)
        """
        Get all neighbors (edges) of a vertex
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex
        """
        # Create an empty queue and enqueue the starting_vertex
        # Create an empty set to track visited vertices

        # while the queue is not empty:
            # get the current vertex (deque from queue)
            # check if the current vertex has not been visited:
                # print the current vertex

                # mark the current vertex as visitied
                    # add the current vertex to a visited_set

                # queue up all the current vertex's neighbors (so we can visit them next)

    def dft(self, starting_vertex):# Going to the nth number on a path and then goes back up and to another if it does not work
        """
        Print each vertex in depth-first order
        beginning from starting_vertex
        """
        # Create an empty stack and enqueue the starting_vertex
        # Create an empty set to track visited vertices

        # while the stack is not empty:
            # get the current vertex (pop from stack)

            # check if the current vertex has not been visited:
                # print the current vertex
                # mark the current vertex as visitied
                    # add the current vertex to a visited_set

                # push up all the current vertex's neighbors (so we can visit them next)

        pass # TODO

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex

        This should be done using recursion
        """
        pass # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breadth_first order.
        """
        # Create an empty queue and enqueue the path to the starting_vertex
        # Create an empty set to track visited vertices

        # while the queue is not empty:
            # get the current vertex path(deque from queue)
            # set the current vertex to the last element of the path

            # check if the current vertex has not been visited:

                # check if the current vertex is destination
                # if it is, stop and return

                # Mark the current vertex as visited
                    # add the current vertex to a visited_set

                # queue up new paths with each neighbor:
                    # take current path
                    # append the neighbor to it
                    # queue up new path

        pass #TODO

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass #TODO


if __name__ == "__main__":
    graph = Graph() # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png

    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    """
    Should print:
    {1:{2}, 2:{3,4}, 3:{5}, 4:{6,7}, 5:{3}, 6:{3}, 7:{1,6}}
    """

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))

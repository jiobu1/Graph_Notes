"""
You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from
cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.
It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly
one destination city.

Example 1:

Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo"
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city.
Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

Example 2:

Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are:
"D" -> "B" -> "C" -> "A".
"B" -> "C" -> "A".
"C" -> "A".
"A".
Clearly the destination city is "A".

Example 3:

Input: paths = [["A","Z"]]
Output: "Z"

Constraints:

    1 <= paths.length <= 100
    paths[i].length == 2
    1 <= cityAi.length, cityBi.length <= 10
    cityAi != cityBi
    All strings consist of lowercase and uppercase English letters and the space character.

Plan:
1. Translate the problem into graph terminology
vertex = cities
edges = paths from city to city
weights = no

2. Build your graph
use an adjacency list, where each key is an origin city,
the values will be its neighboring cities that it has a route to

3.  Traverse the graph
BF/DS does it matter? nope
"""
from collections import deque

class Solution:
    def destCity(self, paths):
        if len(paths) == 0:
            return " "
        graph = self.createGraph(paths)
        stack = deque()
        stack.append(paths[0][0])
        visited = set()
        while len(stack) > 0:
            curr = stack.pop()
            visited.add(curr)
            if curr not in graph:
                return curr
            else:
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        stack.append(neighbor)
        return ""


    def createGraph(self, paths):
        graph = {}
        for edge in paths:
            origin, destination = edge[0], edge[1]
            if origin in graph:
                graph[origin].add(destination)
            else:
                graph[origin] = {destination}
        return graph

paths = [
    ["London", "New York"], 
    ["New York", "Lima"],
    ["Lima", "Sao Paulo"]
]

s = Solution()
print(s.destCity(paths))
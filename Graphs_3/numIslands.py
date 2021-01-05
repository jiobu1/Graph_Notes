"""
Given an m x n 2d grid map of '1's (land) and '0's
(water), return the number of islands.

An island is surrounded by water and is formed by
connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all
surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.

Plan
traverse the grid, wherever you find land, traverse its connected component and mark them as visited.
keep track of number of islands/connected components found
return its count

"""
from collections import deque

class Solution:
    res = 0

    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        width, height = len(grid[0]), len(grid)
        visited = [[False] * width for x in range(height)]
        for y in range(height):
            for x in range(width):
                if grid[y][x] == '1' and not visited[y][x]:
                    self.res += 1
                    self.iterativeDFS(grid, visited, x, y)
        return self.res

    def iterativeDFS(self, grid, visited, x, y):
        width, height = len(grid[0]), len(grid)
        stack = deque()
        stack.append((x, y))
        while len(stack) > 0:
            x, y = stack.pop()
            if visited[y][x]:
                continue
            visited[y][x] = True
            if x - 1 >= 0 and grid[y][x - 1] == '1':
                stack.append((x - 1, y))
            if x + 1 < width and grid[y][x + 1] == '1':
                stack.append((x + 1, y))
            if y - 1 >= 0 and grid[y - 1][x] == '1':
                stack.append((x, y - 1))
            if y + 1 < height and grid[y + 1][x] == '1':
                stack.append((x, y + 1))

    def recursiveDFS(self, grid, visited, x, y):
        width, height = len(grid[0]), len(grid)
        if x < 0 or y < 0 or x >= width or y >= height or grid[y][x] == '0' or visited[y][x]:
            return
        visited[y][x] = True
        self.dfs(grid, visited, x + 1, y)
        self.dfs(grid, visited, x - 1, y)
        self.dfs(grid, visited, x, y + 1)
        self.dfs(grid, visited, x, y - 1)

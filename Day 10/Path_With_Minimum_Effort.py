from typing import List
from collections import deque

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(limit):
            visited = set()
            visited.add((0, 0))
            queue = deque([(0, 0)])

            while queue:
                row, col = queue.popleft()

                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc

                    if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited:
                        if abs(heights[new_row][new_col] - heights[row][col]) <= limit:
                            if (new_row, new_col) == (rows - 1, cols - 1):
                                return True

                            visited.add((new_row, new_col))
                            queue.append((new_row, new_col))

            return False

        left, right = 0, int(1e9)
        result = 0 if rows == 1 and cols == 1 else -1  

        while left <= right:
            mid = left + (right - left) // 2

            if bfs(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result

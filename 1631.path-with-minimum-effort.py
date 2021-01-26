"""
Description: Path With Minimum Effort
Version: 1
Author: Taki Guan
Date: 2021-01-26 22:20:58
LastEditors: Taki Guan
LastEditTime: 2021-01-26 22:58:13
"""
#
# @lc app=leetcode id=1631 lang=python3
#
# [1631] Path With Minimum Effort
#

# @lc code=start
from typing import List
from heapq import heappop, heappush


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        pq = [(0, (0, 0))]
        # 记录该单元格是否已经走过
        visited = [[False] * n for _ in range(m)]
        while True:
            cost, (x, y) = heappop(pq)
            if visited[x][y]:
                continue
            if x == m - 1 and y == n - 1:
                return cost
            visited[x][y] = True
            for i in range(len(dx)):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    heappush(
                        pq, (max(cost, abs(heights[x][y] - heights[nx][ny])), (nx, ny))
                    )
            # print(pq)
        return -1


# @lc code=end

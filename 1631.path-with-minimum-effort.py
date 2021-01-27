"""
Description: Path With Minimum Effort
Version: 1
Author: Taki Guan
Date: 2021-01-26 22:20:58
LastEditors: Taki Guan
LastEditTime: 2021-01-27 08:14:27
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
        if not heights:
            return 0

        m, n = len(heights), len(heights[0])
        # 上下左右四次尝试
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        pq = [(0, (0, 0))]
        # 记录该单元格是否已经走过
        visited = [[False] * n for _ in range(m)]
        while True:
            # 取出堆中的最小元素，默认使用元组第一个元素排序，这里是用cost进行排序
            cost, (x, y) = heappop(pq)
            # print(cost, x, y)
            if visited[x][y]:
                continue
            # 到达终点，返回cost
            if x == m - 1 and y == n - 1:
                return cost
            visited[x][y] = True
            # 对cost最小元素进行上下左右四次位移
            for i in range(len(dx)):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    # 将未访问到的节点放入堆中
                    heappush(
                        pq, (max(cost, abs(heights[x][y] - heights[nx][ny])), (nx, ny))
                    )
            # print(pq)
        return 0


# @lc code=end

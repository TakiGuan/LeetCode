"""
Description: Is Graph Bipartite
Version: 1
Author: Taki Guan
Date: 2021-02-14 20:45:06
LastEditors: Taki Guan
LastEditTime: 2021-02-21 08:34:55
"""
#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#

# @lc code=start
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}

        def dfs(pos):
            for i in graph[pos]:
                if i in color:
                    if color[i] == color[pos]:
                        return False
                else:
                    color[i] = 1 - color[pos]
                    if not dfs(i):
                        return False
            return True

        for i in range(len(graph)):
            if i not in color:
                color[i] = 0
                if not dfs(i):
                    return False
        return True


# @lc code=end

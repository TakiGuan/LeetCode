"""
Description: Brick Wall
Version: 1
Author: Taki Guan
Date: 2021-04-23 10:17:24
LastEditors: Taki Guan
LastEditTime: 2021-04-23 10:24:10
"""
#
# @lc app=leetcode id=554 lang=python3
#
# [554] Brick Wall
#

# @lc code=start
from typing import List
from collections import defaultdict
from itertools import accumulate


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edges, maxEdges = defaultdict(int), 0
        for row in wall:
            for idx in accumulate(row[:-1]):
                edges[idx] += 1
                maxEdges = max(maxEdges, edges[idx])
            # print(edges)
        return len(wall) - maxEdges


# @lc code=end

"""
Description: Shortest Distance to a Character
Version: 1
Author: Taki Guan
Date: 2021-02-07 22:21:49
LastEditors: Taki Guan
LastEditTime: 2021-02-07 22:45:39
"""
#
# @lc app=leetcode id=821 lang=python3
#
# [821] Shortest Distance to a Character
#

# @lc code=start
from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        """
        从0到n-1, 再从n-1到0对s进行两次遍历
        第一遍找右侧最近的c，第二遍找左侧最近的c
        """
        n, pos = len(s), -float("inf")
        res = [n] * n
        for i in tuple(range(n)) + tuple(range(n))[::-1]:
            if s[i] == c:
                pos = i
            res[i] = min(res[i], abs(i - pos))
        return res


# @lc code=end

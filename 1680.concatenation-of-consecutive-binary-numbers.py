"""
Description: Concatenation of Consecutive Binary Numbers
Version: 1
Author: Taki Guan
Date: 2021-01-27 22:30:23
LastEditors: Taki Guan
LastEditTime: 2021-01-27 22:30:53
"""
#
# @lc app=leetcode id=1680 lang=python3
#
# [1680] Concatenation of Consecutive Binary Numbers
#

# @lc code=start
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ret = ""
        for i in range(1, n + 1):
            ret += bin(i)[2:]
        return int(ret, 2) % (10 ** 9 + 7)


# @lc code=end

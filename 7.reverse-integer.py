'''
Description: Reverse Integer
Version: 1
Author: Taki Guan
Date: 2020-12-30 13:15:16
LastEditors: Taki Guan
LastEditTime: 2020-12-30 13:40:29
'''
#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start

# 需要考虑符号和溢出


class Solution:
    def reverse(self, x: int) -> int:
        s = -1 if x < 0 else 1
        r = s * int(str(abs(x))[::-1])
        return r if r >= - 2**31 and r <= (2**31 - 1) else 0

# @lc code=end

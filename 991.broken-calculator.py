"""
Description: Broken Calculator
Version: 1
Author: Taki Guan
Date: 2021-02-22 08:13:10
LastEditors: Taki Guan
LastEditTime: 2021-02-22 08:59:35
"""
#
# @lc app=leetcode id=991 lang=python3
#
# [991] Broken Calculator
#

# @lc code=start
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        ans = 0

        while X < Y:
            ans += Y % 2 + 1
            if Y % 2 == 1:
                Y = (Y + 1) // 2
            else:
                Y = Y // 2
        return ans + X - Y


# @lc code=end

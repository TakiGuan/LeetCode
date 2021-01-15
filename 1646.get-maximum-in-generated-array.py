"""
Description: Get Maximum in Generated Array
Version: 1
Author: Taki Guan
Date: 2021-01-15 22:06:10
LastEditors: Taki Guan
LastEditTime: 2021-01-15 22:18:46
"""
#
# @lc app=leetcode id=1646 lang=python3
#
# [1646] Get Maximum in Generated Array
#

# @lc code=start
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        def calc(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n % 2 == 0:
                return calc(n / 2)
            if n % 2 == 1:
                return calc((n - 1) / 2) + calc((n - 1) / 2 + 1)

        return max(calc(i) for i in range(n + 1))


# @lc code=end

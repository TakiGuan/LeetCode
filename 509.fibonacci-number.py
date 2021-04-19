"""
Description: Fibonacci Number
Version: 1
Author: Taki Guan
Date: 2021-04-16 10:00:47
LastEditors: Taki Guan
LastEditTime: 2021-04-16 10:03:37
"""
#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        # Solution 1
        # if n > 1:
        #     return self.fib(n - 1) + self.fib(n - 2)
        # else:
        #     return n
        # Solution 2
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a


# @lc code=end

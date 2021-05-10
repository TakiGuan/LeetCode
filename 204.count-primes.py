"""
Description: Count Primes
Version: 1
Author: Taki Guan
Date: 2021-05-10 15:07:34
LastEditors: Taki Guan
LastEditTime: 2021-05-10 15:07:58
"""
#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start
import math


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0

        # 构建长度为n的数组
        l = [1] * n
        l[0] = l[1] = 0

        for i in range(2, int(math.sqrt(n) + 1)):
            if l[i] == 1:
                l[i * i : n : i] = [0] * len(l[i * i : n : i])

        return sum(l)


# @lc code=end

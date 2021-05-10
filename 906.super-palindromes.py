"""
Description: Super Palindromes
Version: 1
Author: Taki Guan
Date: 2021-05-08 15:37:17
LastEditors: Taki Guan
LastEditTime: 2021-05-10 09:31:35
"""
#
# @lc app=leetcode id=906 lang=python3
#
# [906] Super Palindromes
#

# @lc code=start
import math


class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        left = int(left)
        right = int(right)

        # print(left, right)

        # L = int(math.sqrt(left))
        # R = int(math.sqrt(right))

        n1 = len(str(int(math.sqrt(left))))
        n2 = len(str(int(math.sqrt(right))))

        n1, n2 = (n1 - 1) // 2 + 1, (n2 - 1) // 2 + 1

        # print(n1, n2)

        start = 10 ** (n1 - 1)
        end = 10 ** n2

        # print(start, end)

        ans = 0

        for i in range(start, end):
            x = str(i)
            num1 = int(x + x[::-1])  # 偶数
            num2 = int(x + x[:-1][::-1])  # 奇数
            for num in [num1, num2]:
                cand = num * num
                if left <= cand <= right and str(cand) == str(cand)[::-1]:
                    ans += 1
        return ans


# @lc code=end

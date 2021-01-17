"""
Description: ount Sorted Vowel Strings
Version: 1
Author: Taki Guan
Date: 2021-01-17 20:23:18
LastEditors: Taki Guan
LastEditTime: 2021-01-17 20:23:40
"""
#
# @lc app=leetcode id=1641 lang=python3
#
# [1641] Count Sorted Vowel Strings
#

# @lc code=start
# |       | a  | e  | i  | o | u |
# | n = 1 | 5  | 4  | 3  | 2 | 1 |
# | n = 2 | 15 | 10 | 6  | 3 | 1 |
# | n = 3 | 35 | 20 | 10 | 4 | 1 |
class Solution:
    def countVowelStrings(self, n: int) -> int:
        # 初始化二维数组
        dp = [[i for i in range(5, 0, -1)] for _ in range(n)]

        # 根据规律计算对应的值
        for i in range(1, n):
            for j in range(3, -1, -1):
                dp[i][j] = dp[i - 1][j] + dp[i][j + 1]
        # 返回最后一行第一列
        return dp[n - 1][0]


# @lc code=end

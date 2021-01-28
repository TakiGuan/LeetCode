"""
Description: Smallest String With A Given Numeric Value
Version: 1
Author: Taki Guan
Date: 2021-01-28 21:29:14
LastEditors: Taki Guan
LastEditTime: 2021-01-28 21:29:44
"""
#
# @lc app=leetcode id=1663 lang=python3
#
# [1663] Smallest String With A Given Numeric Value
#

# @lc code=start
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        # z的数量和剩余的一个字母的位置
        z, r = divmod(k - n - 1, 25)
        # 需要补a的数量，用n减去z的数量和一个其他字母
        a = n - z - 1
        # ord返回字母的unicode码，chr根据unicode码转成字符
        return a * "a" + chr(r + 1 + ord("a")) + z * "z"


# @lc code=end

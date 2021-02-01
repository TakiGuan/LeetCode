"""
Description: Number of 1 Bits
Version: 1
Author: Taki Guan
Date: 2021-02-01 20:54:31
LastEditors: Taki Guan
LastEditTime: 2021-02-01 20:57:18
"""
#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)[2:]
        cnt = 0
        for l in binary:
            if l == "1":
                cnt += 1
        return cnt


# @lc code=end

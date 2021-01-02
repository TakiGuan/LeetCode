'''
Description: Longest Common Prefix
Version: 1
Author: Taki Guan
Date: 2021-01-02 10:37:52
LastEditors: Taki Guan
LastEditTime: 2021-01-02 10:48:35
'''
#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        short = min(strs, key=len)
        # print(short)
        for i, s in enumerate(short):
            for oth in strs:
                if s != oth[i]:
                    return short[:i]
        return short

# @lc code=end

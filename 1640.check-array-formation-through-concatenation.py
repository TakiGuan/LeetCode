'''
Description: Check Array Formation Through Concatenation
Version: 1
Author: Taki Guan
Date: 2021-01-01 16:44:30
LastEditors: Taki Guan
LastEditTime: 2021-01-01 17:19:23
'''
#
# @lc app=leetcode id=1640 lang=python3
#
# [1640] Check Array Formation Through Concatenation
#

# @lc code=start
from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        # arr的每个元素需要是pieces每个元素的首字母
        mp = {x[0]: x for x in pieces}
        ret = []

        for a in arr:
            ret += mp.get(a, [])

        return ret == arr

# @lc code=end

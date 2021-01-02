'''
Description: Reverse String Solution
Version: 1
Author: Taki Guan
Date: 2020-12-30 09:33:38
LastEditors: Taki Guan
LastEditTime: 2020-12-30 09:38:05
'''
#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n//2):
            s[i], s[n-i-1] = s[n-i-1], s[i]

# @lc code=end

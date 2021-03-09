"""
Description: Remove Palindromic Subsequences
Version: 1
Author: Taki Guan
Date: 2021-03-09 08:39:49
LastEditors: Taki Guan
LastEditTime: 2021-03-09 10:04:07
"""
#
# @lc app=leetcode id=1332 lang=python3
#
# [1332] Remove Palindromic Subsequences
#

# @lc code=start
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return (s != "") + (s != s[::-1])


# @lc code=end

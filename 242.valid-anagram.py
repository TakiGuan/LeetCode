'''
Description: Valid Anagram Solution
Version: 1
Author: Taki Guan
Date: 2020-12-30 14:16:48
LastEditors: Taki Guan
LastEditTime: 2020-12-30 14:36:42
'''
#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
import string


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return all([s.count(l) == t.count(l) for l in string.ascii_lowercase])


# @lc code=end

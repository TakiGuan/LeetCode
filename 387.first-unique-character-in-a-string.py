'''
Description: First Unique Character in a String Solution
Version: 1
Author: Taki Guan
Date: 2020-12-30 13:41:55
LastEditors: Taki Guan
LastEditTime: 2020-12-30 14:15:14
'''
#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start

# index is a C function so it's quick

import string


class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters = string.ascii_lowercase
        index = [s.index(l) for l in letters if s.count(l) == 1]
        return min(index, default=-1)


# @lc code=end

"""
Description: Roman to Integer
Version: 1
Author: Taki Guan
Date: 2021-02-21 10:42:33
LastEditors: Taki Guan
LastEditTime: 2021-02-21 10:43:13
"""
#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        _dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        res, i = 0, 0
        for i in range(len(s)):
            curr, next = s[i], s[i + 1 : i + 2]
            if next and _dict[curr] < _dict[next]:
                res -= _dict[curr]
            else:
                res += _dict[curr]
        return res


# @lc code=end

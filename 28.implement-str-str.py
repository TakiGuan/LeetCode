'''
Description: Implement strStr() Solution
Version: 1
Author: Taki Guan
Date: 2021-01-01 19:34:40
LastEditors: Taki Guan
LastEditTime: 2021-01-01 20:01:43
'''
#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0

        lh = len(haystack)
        ln = len(needle)

        for i in range(lh-ln+1):
            if haystack[i:i+ln] == needle:
                return i

        return -1


# @lc code=end

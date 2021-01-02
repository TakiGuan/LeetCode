'''
Description: String to Integer Solution
Version: 1
Author: Taki Guan
Date: 2020-12-31 16:20:11
LastEditors: Taki Guan
LastEditTime: 2020-12-31 16:42:57
'''
#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start


class Solution:
    def myAtoi(self, s: str) -> int:
        # if len(s) == 0:
        #     return 0
        l = list(s.strip())
        if len(l) == 0:
            return 0

        sign = -1 if l[0] == '-' else 1
        # 只解决了首字母为+,-号的问题
        if l[0] in ['+', '-']:
            del l[0]
        n = len(l)
        ret, i = 0, 0

        # 首字符如果不是数字，直接不满足条件
        while i < n and l[i].isdigit():
            ret = ret*10 + int(l[i])
            i += 1

        return max(-2**31, min(sign*ret, 2**31-1))
# @lc code=end

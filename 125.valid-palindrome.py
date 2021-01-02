'''
Description: Palindrome Solution
Version: 1
Author: Taki Guan
Date: 2020-12-31 08:44:37
LastEditors: Taki Guan
LastEditTime: 2020-12-31 14:08:46
'''
#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 正则表达式有问题，r'\w'包含'_'
        s = ''.join(re.findall(r'[0-9a-zA-Z]', s.lower()))
        # print(s)
        return s[::] == s[::-1]


# @lc code=end

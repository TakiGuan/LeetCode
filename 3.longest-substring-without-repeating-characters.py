"""
Description: Longest Substring Without Repeating Characters
Version: 1
Author: Taki Guan
Date: 2021-01-07 22:40:00
LastEditors: Taki Guan
LastEditTime: 2021-01-07 22:40:24
"""
#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        longest = start = 0

        for i, character in enumerate(s):
            # 如果当前字符存在字典中并且该字符的index在start后面，才考虑更新start位置
            # 意思就是只考虑start之后重复的字符
            if character in used and start <= used[character]:
                # start从上次出现的位置前移一步
                start = used[character] + 1
                # print("Start: ", start)
            else:
                # 如果当前字符不存在字典中，用当前位置减去start位置与历史最长长度比较，更新最长
                longest = max(longest, i - start + 1)
                # print("Longest: ", longest)

            # 更新字典
            used[character] = i

        return longest


# @lc code=end

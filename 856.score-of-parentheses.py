"""
Description: Score of Parentheses
Version: 1
Author: Taki Guan
Date: 2021-02-24 21:17:07
LastEditors: Taki Guan
LastEditTime: 2021-02-25 09:27:51
"""
#
# @lc app=leetcode id=856 lang=python3
#
# [856] Score of Parentheses
#

# @lc code=start
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = [0]
        for c in S:
            if c == "(":
                stack.append(0)
            else:
                last = stack.pop()
                # 当last为0时，则stack[-1]加1，否则则加上last * 2
                stack[-1] += last * 2 or 1

        return stack.pop()


# @lc code=end

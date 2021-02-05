"""
Description: Simplify Path
Version: 1
Author: Taki Guan
Date: 2021-02-05 23:02:02
LastEditors: Taki Guan
LastEditTime: 2021-02-05 23:13:01
"""
#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for p in path.split("/"):
            if p == "..":
                if stack:
                    stack.pop()
            elif p and p != ".":
                stack.append(p)

        return "/" + "/".join(stack)


# @lc code=end

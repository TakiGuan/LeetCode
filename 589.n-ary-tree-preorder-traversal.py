"""
Description: N-ary Tree Preorder Traversal
Version: 1
Author: Taki Guan
Date: 2021-04-21 08:40:29
LastEditors: Taki Guan
LastEditTime: 2021-04-21 08:41:22
"""
#
# @lc app=leetcode id=589 lang=python3
#
# [589] N-ary Tree Preorder Traversal
#

# @lc code=start
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


from typing import List


class Solution:
    def preorder(self, root: "Node", ans: List = None) -> List[int]:
        if not root:
            return ans
        if ans == None:
            ans = []
        ans.append(root.val)
        for child in root.children:
            self.preorder(child, ans)
        return ans


# @lc code=end

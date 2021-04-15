"""
Description: Deepest Leaves Sum
Version: 1
Author: Taki Guan
Date: 2021-04-12 14:00:19
LastEditors: Taki Guan
LastEditTime: 2021-04-12 14:01:19
"""
#
# @lc app=leetcode id=1302 lang=python3
#
# [1302] Deepest Leaves Sum
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        curr = [root]
        while curr:
            prev, curr = curr, [
                child for node in curr for child in [node.left, node.right] if child
            ]
        # 当curr为空时， prev为最深的叶节点
        return sum(node.val for node in prev)


# @lc code=end

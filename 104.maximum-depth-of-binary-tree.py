"""
Description: Maximum Depth of Binary Tree
Version: 1
Author: Taki Guan
Date: 2021-01-08 21:30:05
LastEditors: Taki Guan
LastEditTime: 2021-01-08 21:35:34
"""
#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 递归思路，当root不为空时，往下一层，取左右节点中的较大值返回并加1
        if root:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        else:
            return 0


# @lc code=end

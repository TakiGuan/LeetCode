"""
Description: Validate Binary Search Tree
Version: 1
Author: Taki Guan
Date: 2021-01-09 10:33:48
LastEditors: Taki Guan
LastEditTime: 2021-01-09 11:51:06
"""
#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkBST(self, node, left, right):
        # 如果为空返回true
        if not node:
            return True
        # 如果值超出最大最小值，返回false
        if not left < node.val < right:
            return False
        # 递归，对于左侧，比较最小值和中间点的值，对于右侧，比较中间点的值和最大值
        return self.checkBST(node.left, left, node.val) and self.checkBST(
            node.right, node.val, right
        )

    def isValidBST(self, root: TreeNode) -> bool:
        return self.checkBST(root, float("-inf"), float("inf"))


# @lc code=end

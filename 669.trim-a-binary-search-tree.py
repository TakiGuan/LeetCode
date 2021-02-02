"""
Description: Trim a Binary Search Tree
Version: 1
Author: Taki Guan
Date: 2021-02-02 19:30:42
LastEditors: Taki Guan
LastEditTime: 2021-02-02 19:47:25
"""
#
# @lc app=leetcode id=669 lang=python3
#
# [669] Trim a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        # 如果root为空，则返回None
        if not root:
            return None
        # if root.val < low and root.val > high:
        #     return None

        # 如果当前值比low小，则只需要判断右边的树
        if root.val < low:
            return self.trimBST(root.right, low, high)
        # 如果当前值比high大，那么只需要判断左边的树
        elif root.val > high:
            return self.trimBST(root.left, low, high)
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)

        return root


# @lc code=end

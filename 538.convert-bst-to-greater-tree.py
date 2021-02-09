"""
Description: Convert BST to Greater Tree
Version: 1
Author: Taki Guan
Date: 2021-02-09 21:47:25
LastEditors: Taki Guan
LastEditTime: 2021-02-09 21:47:52
"""
#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    sums = 0

    def convertBST(self, root: TreeNode) -> TreeNode:
        """
        用递归思路解决问题，每个元素的值等于自身及右侧元素总和
        """
        if not root:
            return None
        self.convertBST(root.right)
        self.sums += root.val
        root.val = self.sums
        self.convertBST(root.left)

        return root


# @lc code=end

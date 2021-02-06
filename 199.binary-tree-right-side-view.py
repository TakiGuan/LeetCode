"""
Description: Binary Tree Right Side View
Version: 1
Author: Taki Guan
Date: 2021-02-06 20:15:48
LastEditors: Taki Guan
LastEditTime: 2021-02-06 20:16:26
"""
#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        """
        对右侧元素和左侧元素分别回归调用该方法，根据题目含义，只返回从右侧能看到的元素：
        - 优先返回右侧元素
        - 当右侧节点不存在时，返回左侧节点
        """
        if not root:
            return []

        right = self.rightSideView(root.right)
        left = self.rightSideView(root.left)

        return [root.val] + right + left[len(right) :]


# @lc code=end

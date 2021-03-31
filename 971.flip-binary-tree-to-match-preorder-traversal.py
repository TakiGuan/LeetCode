"""
Description: Flip Binary Tree To Match Preorder Traversal
Version: 1
Author: Taki Guan
Date: 2021-03-30 08:30:04
LastEditors: Taki Guan
LastEditTime: 2021-03-31 09:14:31
"""
#
# @lc app=leetcode id=971 lang=python3
#
# [971] Flip Binary Tree To Match Preorder Traversal
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
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        # 结果列表
        res = []
        stack = [root]
        # print(stack)
        i = 0
        while stack:
            node = stack.pop()
            if not node:
                continue
            # 当根节点不相符时，不存在可以通过反转得到voyage的方法
            if node and node.val != voyage[i]:
                return [-1]
            # 在voyage中前进一位，理论上应该是左侧节点
            i += 1
            if node.right and node.right.val == voyage[i]:
                # 当节点右侧不为空且右侧与voyage[i]相等
                # 表明右侧节点在voyage中在左侧，需要在res中添加当前节点
                if node.left:
                    res.append(node.val)
                # 对node的左侧和右侧再进行递归，优先右侧节点，因为我们已知右侧节点在voyage中已经被转移到左侧
                stack.extend([node.left, node.right])
            else:
                # 递归，优先从左侧节点开始
                stack.extend([node.right, node.left])
        return res


# @lc code=end

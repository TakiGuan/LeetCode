"""
Description: Add One Row to Tree
Version: 1
Author: Taki Guan
Date: 2021-03-10 08:34:28
LastEditors: Taki Guan
LastEditTime: 2021-03-10 08:35:01
"""
#
# @lc app=leetcode id=623 lang=python3
#
# [623] Add One Row to Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        def dfs(node, h, dr):
            # 达到插入的层数，根据v值创建新的TreeNode，并根据direction连接新的left和right节点，并返回构建的新TreeNode
            if h == d:
                temp = TreeNode(v)
                if dr == 0:
                    temp.left = node
                if dr == 1:
                    temp.right = node
                return temp

            # 如果为空，直接返回
            if not node:
                return node

            # 如果没有达到对应层数，则往下一层
            node.left = dfs(node.left, h + 1, 0)
            node.right = dfs(node.right, h + 1, 1)

            # 返回最终结果
            return node

        # 从第一层左侧数开始遍历
        return dfs(root, 1, 0)


# @lc code=end

"""
Description: Vertical Order Traversal of a Binary Tree
Version: 1
Author: Taki Guan
Date: 2021-01-29 21:42:22
LastEditors: Taki Guan
LastEditTime: 2021-01-29 21:42:58
"""
#
# @lc app=leetcode id=987 lang=python3
#
# [987] Vertical Order Traversal of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
from typing import List
from collections import defaultdict
from heapq import heappush, heappop


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        maf = defaultdict(list)

        def traverse(node, x, y):
            if not node:
                return

            maf[x].append((y, node.val))
            traverse(node.left, x - 1, y + 1)
            traverse(node.right, x + 1, y + 1)

        traverse(root, 0, 0)
        heap, ans = [], []

        for x, lst in maf.items():
            heappush(heap, (x, sorted(lst)))

        while heap:
            ans.append([v for _, v in heappop(heap)[1]])

        return ans


# @lc code=end

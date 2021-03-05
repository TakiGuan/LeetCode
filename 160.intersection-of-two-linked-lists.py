"""
Description: Intersection of Two Linked Lists
Version: 1
Author: Taki Guan
Date: 2021-03-05 08:46:29
LastEditors: Taki Guan
LastEditTime: 2021-03-05 08:46:52
"""
#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p1, p2 = headA, headB

        while p1 != p2:
            if not p1:
                p1 = headB
            else:
                p1 = p1.next
            if not p2:
                p2 = headA
            else:
                p2 = p2.next

        return p1


# @lc code=end

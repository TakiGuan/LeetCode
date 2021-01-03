'''
Description: Reverse Linked List
Version: 1
Author: Taki Guan
Date: 2021-01-03 17:40:59
LastEditors: Taki Guan
LastEditTime: 2021-01-03 18:17:51
'''
#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 迭代
        # prev = None
        # while head:
        #     curr = head
        #     head = head.next
        #     curr.next = prev
        #     prev = curr
        # return prev
        return self.reverse(head)

    # 递归
    def reverse(self, node, prev=None):
        if not node:
            return prev
        curr = node
        node = node.next
        curr.next = prev
        return self.reverse(node, curr)


# @lc code=end

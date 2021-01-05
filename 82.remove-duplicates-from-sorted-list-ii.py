"""
Description: Remove Duplicates from sorted List
Version: 1
Author: Taki Guan
Date: 2021-01-05 20:01:40
LastEditors: Taki Guan
LastEditTime: 2021-01-05 20:13:05
"""
#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        sta = ListNode(0)
        sta.next = head
        # 使用cur作为sta链表的指针
        cur = sta

        while head and head.next:
            if head.val == head.next.val:
                # head作为head链表的指针
                while head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                cur.next = head
            else:
                cur = cur.next
                head = head.next

        return sta.next


# @lc code=end

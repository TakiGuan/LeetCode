"""
Description: Linked List Cycle
Version: 1
Author: Taki Guan
Date: 2021-01-06 21:31:35
LastEditors: Taki Guan
LastEditTime: 2021-01-06 21:32:15
"""
#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 定义快慢两个指针
        fast = slow = head
        # 如果链表没有循环，fast指针会先到结尾跳出循环，否则就会继续循环直到fast和slow重合
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


# @lc code=end

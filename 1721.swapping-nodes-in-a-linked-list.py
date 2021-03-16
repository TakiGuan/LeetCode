"""
Description: Swapping Nodes in a Linked List
Version: 1
Author: Taki Guan
Date: 2021-03-15 10:52:39
LastEditors: Taki Guan
LastEditTime: 2021-03-15 10:57:19
"""
#
# @lc app=leetcode id=1721 lang=python3
#
# [1721] Swapping Nodes in a Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        # 使用双指针分别指向head
        first = last = head
        # 将指针指向第k个链表节点
        for _ in range(1, k):
            first = first.next

        # 将last指针指向倒数第k个链表节点
        stopped = first
        while stopped.next:
            last = last.next
            stopped = stopped.next

        # 交换first和last的值
        first.val, last.val = last.val, first.val

        return head


# @lc code=end

"""
Description: Partition List
Version: 1
Author: Taki Guan
Date: 2021-04-15 09:54:11
LastEditors: Taki Guan
LastEditTime: 2021-04-15 11:34:54
"""
#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # head1用于存放小于x的元素，head2用于存放大于等于x的元素
        head1 = point1 = ListNode(-1)
        head2 = point2 = ListNode(-1)

        while head:
            if head.val < x:
                point1.next = head
                point1 = point1.next
            else:
                point2.next = head
                point2 = point2.next
            head = head.next

        # 将point2最后一位赋值为None
        point2.next = None
        # 将head1和head2连接起来，跳过初始化的第一个节点
        point1.next = head2.next

        # 返回连接后的List，跳过初始化的第一个节点
        return head1.next


# @lc code=end

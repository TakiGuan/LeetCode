'''
Description: Remove Nth Node from the End of List
Version: 1
Author: Taki Guan
Date: 2021-01-02 19:34:49
LastEditors: Taki Guan
LastEditTime: 2021-01-02 20:26:11
'''
#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        i = j = head

        # Move j to the nth position
        for _ in range(n):
            j = j.next

        # If j to the end of the list, return head's next
        if not j:
            return head.next

        # Move i, j until j to the end of the list
        while j.next:
            i = i.next
            j = j.next

        # link i to i's next node
        i.next = i.next.next

        return head

# @lc code=end

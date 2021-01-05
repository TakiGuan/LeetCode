"""
Description: Palindrome Linked List
Version: 1
Author: Taki Guan
Date: 2021-01-04 22:13:39
LastEditors: Taki Guan
LastEditTime: 2021-01-04 22:18:33
"""
#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 通过指针分别指向链表的前一半和后一半
        # 为了保证前后一半数组可以直接比较，需要将前一半链表逆序
        # 构建逆序链表
        rev = None
        # 双指针
        fast = slow = head
        # 遍历链表
        while fast and fast.next:
            # 快速指针每次前进两位
            fast = fast.next.next
            # 慢速指针每次前进一位，同时将链表前一半元素逆序
            rev, rev.next, slow = slow, rev, slow.next
        # 如果是奇数位链表，需要将slow前进一位进行比较
        if fast:
            slow = slow.next
        # 比较rev和slow链表
        while rev and slow.val == rev.val:
            slow = slow.next
            rev = rev.next

        # 如果是回文链表，rev就移动到None，那么not rev返回真，否则返回假
        return not rev


# @lc code=end

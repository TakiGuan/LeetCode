"""
Description: Add Two Numbers
Version: 1
Author: Taki Guan
Date: 2021-01-12 20:03:12
LastEditors: Taki Guan
LastEditTime: 2021-01-12 20:03:46
"""
#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 除以10得到的商
        quotient = 0
        # 返回List
        ret = lst = ListNode(0)

        # 每次除以10得到的商等于进位数，如果商不为0，需要再进行一次循环
        while l1 or l2 or quotient:
            if l1:
                quotient += l1.val
                l1 = l1.next
            if l2:
                quotient += l2.val
                l2 = l2.next
            # 除以10的商和余数
            quotient, remainder = divmod(quotient, 10)
            # print(quotient, remainder)
            lst.next = lst = ListNode(remainder)
        return ret.next


# @lc code=end

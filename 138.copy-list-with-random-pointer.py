"""
Description: Copy List with Random Pointer
Version: 1
Author: Taki Guan
Date: 2021-02-10 21:52:24
LastEditors: Taki Guan
LastEditTime: 2021-02-10 21:53:25
"""
#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Node") -> "Node":
        dic = dict()
        m = n = head
        while m:
            dic[m] = Node(m.val)
            m = m.next
        while n:
            dic[n].next = dic.get(n.next)
            dic[n].random = dic.get(n.random)
            n = n.next
        return dic.get(head)


# @lc code=end

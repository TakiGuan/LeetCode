"""
Description: Design HashMap
Version: 1
Author: Taki Guan
Date: 2021-03-08 08:31:54
LastEditors: Taki Guan
LastEditTime: 2021-03-08 08:51:36
"""
#
# @lc app=leetcode id=706 lang=python3
#
# [706] Design HashMap
#

# @lc code=start
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.hashmap = [None] * self.size

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        idx = key % self.size

        if self.hashmap[idx] == None:
            self.hashmap[idx] = ListNode(key, value)
        else:
            curr = self.hashmap[idx]
            while True:
                if curr.key == key:
                    curr.value = value
                    return
                if curr.next == None:
                    break
                curr = curr.next
            curr.next = ListNode(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        idx = key % self.size
        curr = self.hashmap[idx]
        while curr:
            if curr.key == key:
                return curr.value
            else:
                curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        idx = key % self.size
        curr = prev = self.hashmap[idx]

        # 如果要删除的map为空，则直接返回
        if not curr:
            return

        if curr.key == key:
            # 如果找到节点，则直接跳过该节点
            self.hashmap[idx] = curr.next
        else:
            # 如果未直接找到节点
            curr = curr.next

            while curr:
                if curr.key == key:
                    prev.next = curr.next
                    break
                else:
                    prev, curr = prev.next, curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end

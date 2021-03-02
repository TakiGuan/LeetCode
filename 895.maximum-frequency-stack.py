"""
Description: Maximum Frequency Stack
Version: 1
Author: Taki Guan
Date: 2021-03-01 08:39:28
LastEditors: Taki Guan
LastEditTime: 2021-03-01 09:32:35
"""
#
# @lc app=leetcode id=895 lang=python3
#
# [895] Maximum Frequency Stack
#

# @lc code=start
import collections


class FreqStack:
    def __init__(self):
        # 记录每个元素出现的次数，当push元素时，次数+1，pop元素时，次数-1
        self.freq = collections.Counter()
        # 记录每个出现次数中的元素，当push 5时，m为{1： [5]}，当push 7时，m为{1: [5, 7]}，当再一次push 5时，则m为{1: [5, 7], 2: [5]}
        self.m = collections.defaultdict(list)
        # 记录最大的出现次数
        self.maxf = 0

    def push(self, x: int) -> None:
        """
        push元素需要执行三个操作，更新freq dict，更新m dict，更新max freq
        """
        freq, m = self.freq, self.m
        freq[x] += 1
        self.maxf = max(self.maxf, freq[x])
        m[freq[x]].append(x)

    def pop(self) -> int:
        """
        pop元素同样需要执行三个操作，从m dict中pop元素，更新freq dict，更新max freq
        """
        freq, m, maxf = self.freq, self.m, self.maxf
        x = m[maxf].pop()
        if not m[maxf]:
            self.maxf = maxf - 1
        freq[x] -= 1
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
# @lc code=end

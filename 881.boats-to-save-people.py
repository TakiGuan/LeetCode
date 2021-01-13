"""
Description: Boats to Save People
Version: 1
Author: Taki Guan
Date: 2021-01-13 21:02:24
LastEditors: Taki Guan
LastEditTime: 2021-01-13 21:32:52
"""
#
# @lc app=leetcode id=881 lang=python3
#
# [881] Boats to Save People
#

# @lc code=start
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # 将数组逆序
        people.sort(reverse=True)
        # print(people)
        # 指针分别指向第一个和最后一个元素
        i, j = 0, len(people) - 1
        # 两个指针需要重合
        while i <= j:
            # 将重量小的和重量最大的配对
            if people[i] + people[j] <= limit:
                j -= 1
            # 开一条船
            i += 1
        return i


# @lc code=end

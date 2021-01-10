"""
Description: Create Sorted Array through Instructions
Version: 1
Author: Taki Guan
Date: 2021-01-10 20:17:33
LastEditors: Taki Guan
LastEditTime: 2021-01-10 21:26:51
"""
#
# @lc app=leetcode id=1649 lang=python3
#
# [1649] Create Sorted Array through Instructions
#

# @lc code=start
from typing import List
from sortedcontainers import SortedList


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        sort = SortedList()
        cost = 0

        for item in instructions:
            # bisect left可以获取所有比item小的元素的个数
            # sort list长度减去bisect right可以获取所有比item大的元素个数
            cost += min(sort.bisect_left(item), len(sort) - sort.bisect_right(item))
            sort.add(item)

        return cost % (10 ** 9 + 7)


# @lc code=end

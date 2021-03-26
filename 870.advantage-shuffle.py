"""
Description: Advantage Shuffle
Version: 1
Author: Taki Guan
Date: 2021-03-25 10:40:02
LastEditors: Taki Guan
LastEditTime: 2021-03-25 10:40:25
"""
#
# @lc app=leetcode id=870 lang=python3
#
# [870] Advantage Shuffle
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        # 对A从小到大进行排序
        A = sorted(A)
        # 构建一个字典，存放每个B的元素和对应的大于B的元素
        mapped = defaultdict(list)
        # 对于b中每个元素当找到比它大的A中元素时，将A中元素存入对应的list中
        for b in sorted(B)[::-1]:
            if A[-1] > b:
                mapped[b].append(A.pop())

        # 从mapped中能找到b则返回对应A中元素，否则从A中取
        return [(mapped[b] or A).pop() for b in B]


# @lc code=end

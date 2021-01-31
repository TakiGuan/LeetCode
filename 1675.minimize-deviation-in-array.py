"""
Description: Minimize Deviation in Array
Version: 1
Author: Taki Guan
Date: 2021-01-30 21:22:47
LastEditors: Taki Guan
LastEditTime: 2021-01-31 19:44:10
"""
#
# @lc app=leetcode id=1675 lang=python3
#
# [1675] Minimize Deviation in Array
#

# @lc code=start
from typing import List
from heapq import *


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = []
        # 构建数组，数组中为nums数组中每个元素及这个元素的最小及最大值
        for num in nums:
            if num % 2 == 0:
                n = num
                while n % 2 == 0:
                    n //= 2
                heap.append([n, num])
            else:
                heap.append([num, num * 2])

        # 从最小值中取得最大值
        max_value = max([val[0] for val in heap])
        heapify(heap)
        ans = float("inf")

        while True:
            # 从所有数组中取得最小值中的最小值
            val, bound = heappop(heap)
            # 如果该值超出最大值，则跳出循环
            if val >= bound:
                break
            max_value = max(val * 2, max_value)
            heappush(heap, [val * 2, bound])
            ans = min(ans, max_value - heap[0][0])

        return ans


# @lc code=end

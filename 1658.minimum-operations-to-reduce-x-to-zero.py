"""
Description: Minimum Operations to Reduce X to Zero
Version: 1
Author: Taki Guan
Date: 2021-01-14 21:52:57
LastEditors: Taki Guan
LastEditTime: 2021-01-14 21:53:22
"""
#
# @lc app=leetcode id=1658 lang=python3
#
# [1658] Minimum Operations to Reduce X to Zero
#

# @lc code=start
from typing import List

# 将找最少元素组成x问题转化为最多元素组成sum-x的问题
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n, s, cur, res = len(nums), sum(nums), 0, -1
        # 找出能够组成sum-x的最长组合
        # 字典中存储从左到右累加的和及索引
        tar, dic = s - x, {0: -1, s: n - 1}
        for i, num in enumerate(nums):
            # 从左到右累加元素
            cur += num
            # 当累加值大于目标值时，找出字典中是否存在累加值与目标值的差值
            # 如果存在，那么计算累加的次数，并将当前累加值与历史最大累加值比较
            # 找到历史最大累加值
            if (cur - tar) in dic:
                res = max(res, i - dic[cur - tar])
            dic[cur] = i
        return -1 if res < 0 else n - res


# @lc code=end

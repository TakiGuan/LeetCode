"""
Description: Russian Doll Envelopes
Version: 1
Author: Taki Guan
Date: 2021-03-31 09:24:11
LastEditors: Taki Guan
LastEditTime: 2021-03-31 09:24:39
"""
#
# @lc app=leetcode id=354 lang=python3
#
# [354] Russian Doll Envelopes
#

# @lc code=start
from typing import List
from bisect import bisect_left


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # 按宽度递增，高度递减顺序对envelopes进行排序
        # 之所以按照高度递减顺序排列，是为了避免宽度相同情况会被计算两次
        nums = sorted(envelopes, key=lambda x: [x[0], -x[1]])
        # print(nums)
        # 寻找最长增长子串
        # 初始化nums长度的list，使用非常大的值填充该list
        dp = [10 ** 10] * (len(nums) + 1)
        for elem in nums:
            # 使用二分查找法确定高度插入位置并更新dp列表
            dp[bisect_left(dp, elem[1])] = elem[1]
        # print(dp)
        # 返回第一个非常大的值位置，该位置是最长子串的长度
        return dp.index(10 ** 10)


# @lc code=end

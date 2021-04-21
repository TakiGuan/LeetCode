"""
Description: Combination Sum IV
Version: 1
Author: Taki Guan
Date: 2021-04-19 16:27:23
LastEditors: Taki Guan
LastEditTime: 2021-04-20 08:41:54
"""
#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # 生成均为0的List，代表次数均为0
        dp = [0] * (1 + target)
        # 遍历生成的List，当num小于target时，将该数值代表的值设置为1，代表该值可能存在1次
        for num in nums:
            if num <= target:
                dp[num] = 1
        # 从1开始遍历到target，当每次遍历的值减去num列表中的值大于0时，将遍历值代表的次数更新为原值与i-num代表的次数的和
        for i in range(1 + target):
            for num in nums:
                if i - num > 0:
                    dp[i] += dp[i - num]
        return dp[-1]


# @lc code=end

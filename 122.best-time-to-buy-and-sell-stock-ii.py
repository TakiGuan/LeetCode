'''
Description: Best Time to Buy and Sell Stock Solution
Version: 1
Author: Taki Guan
Date: 2020-12-26 17:00:57
LastEditors: Taki Guan
LastEditTime: 2020-12-29 14:33:21
'''
#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += (prices[i] - prices[i - 1])
        return profit


# @lc code=end

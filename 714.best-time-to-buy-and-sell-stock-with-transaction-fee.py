"""
Description: Best Time to Buy and Sell Stock with Transaction Fee
Version: 1
Author: Taki Guan
Date: 2021-03-17 08:39:32
LastEditors: Taki Guan
LastEditTime: 2021-03-17 08:40:25
"""
#
# @lc app=leetcode id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        原则是只要价格高于手续费加当初买入费用则进行交易，如果当天价格不是最高价格则撤销交易
        type prices: List[int]
        type fee: int
        rtype: int
        """
        n = len(prices)
        if n <= 1:
            return 0
        profit = 0
        minimum = prices[0]

        for i in range(1, n):
            if prices[i] < minimum:
                minimum = prices[i]  # 当前最低价格
            elif prices[i] > minimum + fee:  # 如果当前价格大于最低价加上手续费，可以考虑卖出获利
                profit += prices[i] - minimum - fee  # 获利等于当前价格减去买入价格欧减去交易费用
                minimum = prices[i] - fee  # 减去手续费的目的是为了避免后续价格高于当天卖出价格，手续费被重复计算

        return profit


# @lc code=end

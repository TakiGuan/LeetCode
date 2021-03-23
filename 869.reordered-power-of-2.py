"""
Description: Reordered Power of 2
Version: 1
Author: Taki Guan
Date: 2021-03-22 09:12:48
LastEditors: Taki Guan
LastEditTime: 2021-03-22 09:35:26
"""
#
# @lc app=leetcode id=869 lang=python3
#
# [869] Reordered Power of 2
#

# @lc code=start
from collections import Counter


class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        # 统计数字中每个数字出现的次数
        c1 = Counter(str(N))
        for i in range(30):
            # 计算2的0到29次方，并转为对应的字符串，统计每个数字出现的次数
            c2 = Counter(str(2 ** i))
            if c1 == c2:
                return True
        return False


# @lc code=end

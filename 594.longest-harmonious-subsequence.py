"""
Description: Longest Harmonious Subsequence
Version: 1
Author: Taki Guan
Date: 2021-02-04 19:14:38
LastEditors: Taki Guan
LastEditTime: 2021-02-04 19:24:08
"""
#
# @lc app=leetcode id=594 lang=python3
#
# [594] Longest Harmonious Subsequence
#

# @lc code=start
from typing import List
from collections import Counter


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        """
        找到最长的和谐字串，和谐字串是差为1的元素组成的集合

        Parameters:
            nums: 待求数组

        Returns:
            最大集合长度
        """
        count = Counter(nums)
        ans = 0

        for num in count:
            if num + 1 in count:
                ans = max(ans, count[num] + count[num + 1])

        return ans


# @lc code=end

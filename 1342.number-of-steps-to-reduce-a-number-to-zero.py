"""
Description: Number of Steps to Reduce a Number to Zero
Version: 1
Author: Taki Guan
Date: 2021-02-12 17:49:54
LastEditors: Taki Guan
LastEditTime: 2021-02-12 17:50:24
"""
#
# @lc app=leetcode id=1342 lang=python3
#
# [1342] Number of Steps to Reduce a Number to Zero
#

# @lc code=start
class Solution:
    cnt = 0

    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return self.cnt
        if num % 2 == 0:
            self.cnt += 1
            return self.numberOfSteps(num / 2)
        if num % 2 == 1:
            self.cnt += 1
            return self.numberOfSteps(num - 1)

        return self.cnt


# @lc code=end

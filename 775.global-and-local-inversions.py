"""
Description: Global and Local Inversions
Version: 1
Author: Taki Guan
Date: 2021-04-06 13:59:56
LastEditors: Taki Guan
LastEditTime: 2021-04-06 14:00:24
"""
#
# @lc app=leetcode id=775 lang=python3
#
# [775] Global and Local Inversions
#

# @lc code=start
from typing import List


class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        """
        所有的局部变换都属于全局变换
        如果局部变换数量等于全局变换数量，那么所有的A[i]均小于获等于A[i+2]，即max(A[i])<=A[i+2]
        """
        emax = 0
        for i in range(0, len(A) - 2):
            emax = max(emax, A[i])
            if emax > A[i + 2]:
                return False
        return True


# @lc code=end

"""
Description: Power of Three
Version: 1
Author: Taki Guan
Date: 2021-04-28 10:44:18
LastEditors: Taki Guan
LastEditTime: 2021-04-28 10:59:41
"""
#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#

# @lc code=start
class Solution:
    """
    找出允许范围内3的最大幂次
    发现3**19是最接近2**31-1的整数
    """

    def isPowerOfThree(self, n: int) -> bool:
        # return n > 0 and 0 == (3 ** 19 % n)
        return n > 0 == (3 ** 19 % n)


# @lc code=end

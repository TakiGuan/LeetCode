"""
Description: Integer to Roman
Version: 1
Author: Taki Guan
Date: 2021-03-11 09:00:16
LastEditors: Taki Guan
LastEditTime: 2021-03-11 09:16:54
"""
#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        # 定义数据字典
        # Python 3.6 以后字典是有序的
        _dict = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }

        ret = ""

        for d in _dict:
            ret += (num // d) * _dict[d]
            num %= d

        return ret


# @lc code=end

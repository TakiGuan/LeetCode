"""
Description: Reconstruct Original Digits from English
Version: 1
Author: Taki Guan
Date: 2021-03-29 09:41:30
LastEditors: Taki Guan
LastEditTime: 2021-03-29 09:41:57
"""
#
# @lc app=leetcode id=423 lang=python3
#
# [423] Reconstruct Original Digits from English
#

# @lc code=start
class Solution:
    def originalDigits(self, s: str) -> str:
        res = ""
        # z仅仅存在于zero中
        res += "0" * s.count("z")
        # o存在于zero, one, two, four中，其中zero, two, four仅仅含有z, w, u
        res += "1" * (s.count("o") - s.count("z") - s.count("w") - s.count("u"))
        # w仅仅存在于two中
        res += "2" * (s.count("w"))
        # t存在于three, two, eight中，其中two, eight仅仅含有w, g
        res += "3" * (s.count("t") - s.count("w") - s.count("g"))
        # u仅仅存在于four中
        res += "4" * (s.count("u"))
        # f仅仅存在于four, five中
        res += "5" * (s.count("f") - s.count("u"))
        # x仅仅存在于six中
        res += "6" * (s.count("x"))
        # s仅仅存在于six, seven中
        res += "7" * (s.count("s") - s.count("x"))
        # g仅仅存在于eight中
        res += "8" * (s.count("g"))
        # i存在于nine, eight, six, five中
        res += "9" * (
            s.count("i") - s.count("g") - s.count("x") - s.count("f") + s.count("u")
        )
        return res


# @lc code=end

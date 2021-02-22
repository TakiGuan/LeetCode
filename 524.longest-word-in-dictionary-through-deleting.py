"""
Description: Longest Word in Dictionary through Deleting
Version: 1
Author: Taki Guan
Date: 2021-02-22 21:26:59
LastEditors: Taki Guan
LastEditTime: 2021-02-22 21:27:39
"""
#
# @lc app=leetcode id=524 lang=python3
#
# [524] Longest Word in Dictionary through Deleting
#

# @lc code=start
from typing import List


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        # 对字典进行排序，按照长度逆序，字母大小升序排列
        d.sort(key=lambda w: (-len(w), w))
        # 取字典中每个元素
        for w in d:
            # 指针遍历元素
            i = 0
            # 取字符串中每个字母
            for c in s:
                if i < len(w) and w[i] == c:
                    i += 1
            # 如果字符串中存在该元素，则返回该元素
            if i == len(w):
                return w
        return ""


# @lc code=end

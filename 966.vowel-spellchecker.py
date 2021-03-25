"""
Description: Vowel Spellchecker
Version: 1
Author: Taki Guan
Date: 2021-03-23 08:24:18
LastEditors: Taki Guan
LastEditTime: 2021-03-23 08:24:51
"""
#
# @lc app=leetcode id=966 lang=python3
#
# [966] Vowel Spellchecker
#

# @lc code=start
from typing import List
import re


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        # 将List转为字典
        words = {w: w for w in wordlist}
        # 将wordlist每个元素的小写也转为字典
        # 从末尾开始循环是希望最先的元素会覆盖掉末尾的
        caps = {w.lower(): w for w in wordlist[::-1]}
        # 将元音字母剔除转为字典
        vowels = {re.sub("[aeiou]", "#", w.lower()): w for w in wordlist[::-1]}

        # 从words, caps, vowels字典中获取query中的元素，如果存在则返回query中的元素，否则返回空字符串
        return [
            words.get(w) or caps.get(w.lower())
            # 如果最后一个也获取不到则直接返回空字符串
            or vowels.get(re.sub("[aeiou]", "#", w.lower()), "")
            for w in queries
        ]


# @lc code=end

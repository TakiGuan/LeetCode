"""
Description: Stamping The Sequence
Version: 1
Author: Taki Guan
Date: 2021-04-01 10:17:19
LastEditors: Taki Guan
LastEditTime: 2021-04-01 10:18:19
"""
#
# @lc app=leetcode id=936 lang=python3
#
# [936] Stamping The Sequence
#

# @lc code=start
from typing import List


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        s_len, t_len, t_list, s_list, res = (
            len(stamp),
            len(target),
            list(target),
            list(stamp),
            [],
        )

        def check(i):
            changed = False
            # 从i位置逐一对比target和stamp，如果除了已经是?，其余都相同，则进行盖章
            for j in range(s_len):
                # print(i, j)
                if t_list[i + j] == "?":
                    continue
                # print(t_list[i + j], s_list[j], t_list[i + j] != s_list[j])
                if t_list[i + j] != s_list[j]:
                    return False
                changed = True
            # 如果确定盖章，则将已经盖章的位置都赋值为?，且记录当前盖章的位置
            # print(i, changed)
            if changed:
                t_list[i : i + s_len] = ["?"] * s_len
                # print(i)
                # print(t_list)
                res.insert(0, i)
                # res.append(i)
            return changed

        # t_list是否有过变动，只要修改过t_list，则将changed赋值为True，需要再遍历一次t_list
        # 默认第一次为True
        changed = True
        while changed:
            # 默认不进行t_list下一次遍历
            changed = False
            # 对t_list进行遍历，只需要从0遍历到t_len-s_len即可
            for i in range(t_len - s_len + 1):
                # 只要过程中有过一次修改，则默认需要再遍历一次
                changed = changed or check(i)
        # print(res)
        # print(t_list)
        return res if t_list == ["?"] * t_len else []


# @lc code=end

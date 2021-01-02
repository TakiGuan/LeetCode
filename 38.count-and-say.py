'''
Description: Count and Say
Version: 1
Author: Taki Guan
Date: 2021-01-01 21:23:02
LastEditors: Taki Guan
LastEditTime: 2021-01-01 21:46:59
'''
#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start


class Solution:
    def countAndSay(self, n: int) -> str:
        # 当n为1时，返回1
        ret = '1'

        # 当n大于1时执行
        while n > 1:
            # 对ret进行计数
            i = 0
            # 本次计数结果
            tmp = ''
            while i < len(ret):
                # 数字出现次数
                cnt = 1
                while i+1 < len(ret) and ret[i+1] == ret[i]:
                    i += 1
                    cnt += 1
                # 将本次数字出现次数和上次结果相加
                tmp += str(cnt) + ret[i]
                i += 1
            # 将本次计数结果赋给结果字符串，如果循环未结束，对当前字符串重新计数
            ret = tmp
            n -= 1

        return ret

# @lc code=end

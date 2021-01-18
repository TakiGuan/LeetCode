/*
 * @Description: Max Number of K-Sum Pairs
 * @Version: 1
 * @Author: Taki Guan
 * @Date: 2021-01-18 23:17:05
 * @LastEditors: Taki Guan
 * @LastEditTime: 2021-01-19 00:00:41
 */
/*
 * @lc app=leetcode id=1679 lang=typescript
 *
 * [1679] Max Number of K-Sum Pairs
 */

// @lc code=start
function maxOperations(nums: number[], k: number): number {
  let map = getRecordsToMap(nums)
  let ret = 0
  // 如果该元素和k-该元素同时存在，则取该元素与k-该元素中较小的值
  // 作为满足和为k的数量，存在重复计数问题，返回结果要除以2，且向下取整
  for (const i of map.keys()) {
    if (map.has(k - i)) {
      ret += Math.min(map.get(i), map.get(k - i))
    }
  }
  // return Math.floor(ret / 2)
  return ret >> 2
}

// 将nums存为hashset，key为元素，value为出现的次数
const getRecordsToMap = (arr: number[]) => {
  let map = new Map()
  for (const i of arr) {
    map.set(i, map.get(i) + 1 || 1)
  }
  return map
}

// @lc code=end

/*
 * @Description: Determine if Two Strings Are Close
 * @Version: 1
 * @Author: Taki Guan
 * @Date: 2021-01-22 18:28:21
 * @LastEditors: Taki Guan
 * @LastEditTime: 2021-01-22 21:55:43
 */
/*
 * @lc app=leetcode id=1657 lang=typescript
 *
 * [1657] Determine if Two Strings Are Close
 */

// @lc code=start
function closeStrings(word1: string, word2: string): boolean {
  // 长度不同直接返回false
  if (word1.length !== word2.length) return false

  // 两个数组存放word1和word2中从a到z的字符个数
  let arr1 = Array(26).fill(0)
  let arr2 = Array(26).fill(0)

  // 以a为基准值
  const bench = 'a'.charCodeAt(0)

  for (const w1 of word1) {
    arr1[w1.charCodeAt(0) - bench]++
  }
  for (const w2 of word2) {
    arr2[w2.charCodeAt(0) - bench]++
  }

  // 如果某个字符word1中有word2中没有或者word1中没有word2中有则直接返回false
  for (let i = 0; i < 26; i++) {
    if ((arr1[i] === 0 && arr2[i] !== 0) || (arr1[i] !== 0 && arr2[i] === 0))
      return false
  }

  arr1.sort()
  arr2.sort()

  // 如果两个数组字符数不一致则返回false
  for (let i = 0; i < 26; i++) {
    if (arr1[i] !== arr2[i]) return false
  }

  return true
}
// @lc code=end

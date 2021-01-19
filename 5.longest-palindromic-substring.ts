/*
 * @Description: Longest Palindromic Substring
 * @Version: 1
 * @Author: Taki Guan
 * @Date: 2021-01-19 18:07:25
 * @LastEditors: Taki Guan
 * @LastEditTime: 2021-01-19 20:06:20
 */
/*
 * @lc app=leetcode id=5 lang=typescript
 *
 * [5] Longest Palindromic Substring
 */

// @lc code=start
function longestPalindrome(s: string): string {
  let max: string = ''

  for (let i = 0; i < s.length; i++) {
    // j为0判断奇数类型的回文，j为1判断偶数类型的回文
    for (const j of [0, 1]) {
      let left = i
      let right: number = i + j
      while (s[left] && s[left] === s[right]) {
        left--
        right++
      }
      // 用得到的新回文数组和历史数组比较
      max = right - left - 1 > max.length ? s.substring(left + 1, right) : max

      // 如果数组最长的长度一半和目前数组剩余的元素相等，那么现有长度就是最长的长度
      if (max.length >> 1 >= s.length - i) {
        break
      }
    }
  }

  return max
}
// @lc code=end

/*
 * @Description: Find the Most Competitive Subsequence
 * @Version: 1
 * @Author: Taki Guan
 * @Date: 2021-01-21 20:46:34
 * @LastEditors: Taki Guan
 * @LastEditTime: 2021-01-21 21:23:12
 */
/*
 * @lc app=leetcode id=1673 lang=typescript
 *
 * [1673] Find the Most Competitive Subsequence
 */

// @lc code=start
function mostCompetitive(nums: number[], k: number): number[] {
  let n = nums.length
  let stack = []
  // 最后输出stack的长度为k，则最多可移走的元素数量为n-k
  let remove = n - k

  for (const num of nums) {
    // 只要数组元素小于stack中最前一位，则将stack中最前一位取走，不停循环，直至stack中最上一个元素小于当前元素
    // 每移走一个元素，则remove减1
    while (num < stack[stack.length - 1] && remove) {
      stack.pop()
      remove--
    }

    // 将当前元素放入数组
    stack.push(num)
  }

  // 如果stack的长度大于指定长度k，则将最大的元素取走
  while (stack.length > k) stack.pop()

  return stack
}
// @lc code=end

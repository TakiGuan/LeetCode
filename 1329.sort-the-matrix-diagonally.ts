/*
 * @Description: Sort the Matrix Diagonally
 * @Version: 1
 * @Author: Taki Guan
 * @Date: 2021-01-23 20:29:24
 * @LastEditors: Taki Guan
 * @LastEditTime: 2021-01-23 21:12:30
 */
/*
 * @lc app=leetcode id=1329 lang=typescript
 *
 * [1329] Sort the Matrix Diagonally
 */

// @lc code=start
function diagonalSort(mat: number[][]): number[][] {
  // 将同一个斜列的元素放在同一个数组中，数组的key为i-j
  let map = {}

  for (let i = 0; i < mat.length; i++) {
    for (let j = 0; j < mat[i].length; j++) {
      // 计算差值
      let diff = i - j
      // console.log(i, j, diff)
      if (!map[diff]) {
        map[diff] = []
      }
      map[diff].push(mat[i][j])
    }
  }

  for (const key in map) {
    map[key].sort((a: number, b: number) => a - b)
  }

  // console.log(map)

  for (let i = 0; i < mat.length; i++) {
    for (let j = 0; j < mat[i].length; j++) {
      let diff = i - j
      mat[i][j] = map[diff].shift()
    }
  }

  return mat
}
// @lc code=end

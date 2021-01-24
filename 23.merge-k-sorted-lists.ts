/*
 * @Description: Merge k Sorted Lists
 * @Version: 1
 * @Author: Taki Guan
 * @Date: 2021-01-24 21:59:22
 * @LastEditors: Taki Guan
 * @LastEditTime: 2021-01-24 22:15:38
 */
/*
 * @lc app=leetcode id=23 lang=typescript
 *
 * [23] Merge k Sorted Lists
 */

// @lc code=start

// Definition for singly-linked list.
// class ListNode {
//   val: number
//   next: ListNode | null
//   constructor(val?: number, next?: ListNode | null) {
//     this.val = val === undefined ? 0 : val
//     this.next = next === undefined ? null : next
//   }
// }

// 比较两个ListNode，返回比较好的结果
function mergeLists(a: ListNode, b: ListNode) {
  const dummy = new ListNode(0)
  let temp = dummy
  while (a !== null && b !== null) {
    if (a.val < b.val) {
      temp.next = a
      a = a.next
    } else {
      temp.next = b
      b = b.next
    }
    temp = temp.next
  }
  if (a !== null) {
    temp.next = a
  }
  if (b !== null) {
    temp.next = b
  }
  return dummy.next
}

// 对lists中的结果两两比较，直至结果数组中只剩下一个
function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
  if (lists.length === 0) {
    return null
  }

  while (lists.length > 1) {
    let a = lists.shift()
    let b = lists.shift()
    let temp = mergeLists(a, b)
    lists.push(temp)
  }

  return lists[0]
}
// @lc code=end

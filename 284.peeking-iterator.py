"""
Description: Peeking Iterator
Version: 1
Author: Taki Guan
Date: 2021-02-08 22:01:13
LastEditors: Taki Guan
LastEditTime: 2021-02-08 22:15:47
"""
#
# @lc app=leetcode id=284 lang=python3
#
# [284] Peeking Iterator
#

# @lc code=start
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self._iterator = iterator
        self._peek = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self._peek is None:
            self._peek = self._iterator.next()
        return self._peek

    def next(self):
        """
        :rtype: int
        """
        if self._peek is not None:
            val, self._peek = self._peek, None
            return val
        else:
            return self._iterator.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self._iterator.hasNext() or self._peek is not None


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
# @lc code=end

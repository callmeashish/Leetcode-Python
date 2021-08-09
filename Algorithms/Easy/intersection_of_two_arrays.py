"""
349. Intersection of Two Arrays

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""

from typing import List


class Intersection:
    # Algorithmic solution to problem
    def intersection1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        for i in nums1:
            if i in nums2 and i not in stack:
                stack.append(i)

        return stack

    # Python way
    def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))


if __name__ == '__main__':
    a1 = [4, 9, 5]
    a2 = [9, 4, 9, 8, 4]
    print(Intersection().intersection1(a1, a2))
    print(Intersection().intersection2(a1, a2))

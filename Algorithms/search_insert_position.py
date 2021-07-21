"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
Example 4:

Input: nums = [1,3,5,6], target = 0
Output: 0
Example 5:

Input: nums = [1], target = 0
Output: 0
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""

from typing import List


class SearchInputPosition:
    def searchInsertRecusriveBinary(self, nums: List[int], target: int, l: int, r: int):

        if r >= l:

            mid = int((l + r) / 2)

            if len(nums) <= 2 and (nums[mid] >= target and nums[mid - 1] < target):
                return mid

            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                return self.searchInsertRecusriveBinary(nums, target, l, mid - 1)

            else:
                return self.searchInsertRecusriveBinary(nums, target, mid + 1, r)

        else:

            return l

    def searchInsertIterativeBinary(self, nums: List[int], target: int) -> int:

        low = 0
        high = len(nums) - 1
        mid = 0

        while low <= high:

            mid = (high + low) // 2

            if nums[mid] < target:
                low = mid + 1

            elif nums[mid] > target:
                high = mid - 1

            elif nums[mid] == target:
                return mid

            elif len(nums) <= 2 and (nums[mid] >= target and nums[mid - 1] < target):
                return mid

        return low


if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    target = 5
    # Iterative way
    print(SearchInputPosition().searchInsertIterativeBinary(nums, target))

    # Recursive way
    print(
        SearchInputPosition().searchInsertRecusriveBinary(
            nums, target, 0, (len(nums) - 1)
        )
    )

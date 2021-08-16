"""
414. Third Maximum Number

Given integer array nums, return the third maximum number in this array. If the third maximum does not exist, return the maximum number.

 

Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation: The third maximum is 1.

Example 2:

Input: nums = [1,2]
Output: 2
Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Can you find an O(n) solution?
"""


from typing import List


class Max:
    # Algorithmic way
    def thirdMax1(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        fmax = nums[0]
        smax = float("-inf")
        tmax = float("-inf")

        for i in range(n):
            num = nums[i]

            if num > fmax:
                tmax = smax
                smax = fmax
                fmax = num

            elif num > smax and num < fmax:
                tmax = smax
                smax = num

            elif num > tmax and num < smax:
                tmax = num

        return tmax if tmax != float("-inf") else fmax

    # Pythonic way
    def thirdMax2(self, nums: List[int]) -> int:
        nums = set(nums)
        nums = list(nums)
        nums.sort()

        return nums[-3] if len(nums) >= 3 else nums[-1]


if __name__ == "__main__":
    arr = [3, 2, 1]
    print(Max().thirdMax1(arr))
    print(Max().thirdMax2(arr))

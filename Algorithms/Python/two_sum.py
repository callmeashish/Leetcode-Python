from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        values_dict = dict()
        
        for key, value in enumerate(nums):
            complement = target - value
            if complement in values_dict:
                return [values_dict[complement], key]
            values_dict[value] = key
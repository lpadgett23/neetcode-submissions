from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevSeenMap={}

        for i, num in enumerate(nums):
            diff = target - num
            
            if diff in prevSeenMap:
                return [prevSeenMap[diff], i]

            prevSeenMap[num] = i

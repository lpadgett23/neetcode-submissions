class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts={}
        maj_floor = len(nums)//2
        maj=nums[0]
        
        for num in nums:
            counts[num] = counts.get(num, 0) + 1 
            
        for k, v in counts.items():
            if v > maj_floor:
                maj=k
        
        return maj

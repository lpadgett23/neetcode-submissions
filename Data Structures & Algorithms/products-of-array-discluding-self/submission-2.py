class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        zero_count = 0
        prod = 1
        res = [0] * n

        for i in range(n):
            if nums[i] == 0:
                zero_count += 1
                continue
            prod = nums[i] * prod
            
        if zero_count > 1:
            return res

        elif zero_count == 1:
            idx_w_zero = nums.index(0)
            res[idx_w_zero] = prod
            return res
        
        else:
            for j in range(n):
                res[j] = prod // nums[j]

        return res


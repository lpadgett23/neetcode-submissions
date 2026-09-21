class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            fullProduct = 1
            for j in range(len(nums)):
                if j!=i:
                    fullProduct = nums[j] * fullProduct
                    j+=1
            
            output.append(fullProduct)
        
        return output
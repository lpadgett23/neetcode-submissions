class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0,0,0]
        for i in range(len(nums)):
            val = nums[i]
            counts[val] = counts[val] + 1

        red = counts[0]
        white = counts[1]
        blue = counts[2]

        r = 0
        w=red
        b = red + white

        for i in range(red):
            nums[r] = 0
            r+=1

        for i in range(white):
            nums[w] = 1
            w+=1
        
        for i in range(blue):
            nums[b] = 2
            b+=1
        
        return nums
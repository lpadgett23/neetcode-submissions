class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        d=len(nums)
        i=0

        # iterate through nums, swapping or shifting as i go
        while i < d:
            if nums[i] == val:
                d -= 1
                nums[i] = nums[d]
            else:
                i += 1

        return d
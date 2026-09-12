class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # start counts that track what is going on
        k=0
        i=0

        # iterate through nums, replacing the val with _ , update repl count
        for i in range(len(nums)):
            if nums[i] != val:
                k+=1
                continue
            if nums[i] == val:
                nums.append(nums[i])
                nums.pop(i)

        return k
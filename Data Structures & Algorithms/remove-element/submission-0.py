class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # start counts that track what is going on
        len_orig = len(nums)
        replaced_count = 0
        k = 0
        ans = []

        # iterate through nums, replacing the val with _ , update repl count
        for i in range(len(nums)):
            if nums[i] != val:
                ans.append(nums[i])
            if nums[i] == val:
                nums[i] = _
                replaced_count += 1


        k =  len_orig - replaced_count
        replaced_str_for_ans = _ * k
        nums = ans.append(replaced_str_for_ans)
 
        return k
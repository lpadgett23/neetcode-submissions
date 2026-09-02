class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        refset = set()
        for n in nums:
            if n in refset:
                return True
            else:
                refset.add(n)
        return False

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        else:
            mid = len(nums) // 2
            left = self.sortArray(nums[:mid])  # this is returning a NEW sorted list, each half is its own data new data structure(i.e. not an interval represented by pointers)
            right = self.sortArray(nums[mid:])

        res = []
        l, r = 0, 0
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                res.append(left[l])
                l+=1
            else:
                res.append(right[r])
                r+=1

        res.extend(left[l:])
        res.extend(right[r:])

        return res


# this is a functional way of approaching it
# every slice here is actually a deep copy. this takes more memory than a solution approach that uses pointers for indices to represent intervals
# you're doing lots of copying, it is basically allocating new lists at every level (both the lists and at res) 
# so total space worst case is O(nlogn) because per level memory is O(n) and it is across log n levels
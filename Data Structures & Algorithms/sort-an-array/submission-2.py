class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(arr, L, M, R):
            left, right = arr[L:M+1], arr[M+1:R+1]
            i, j, k = L, 0, 0           # i will be the pointer on nums, j is pointer on left and k is pointer for right

            while j < len(left) and k < len(right):    # so while they are each in bounds
                if left[j] <= right[k]:   # make sure that integer with integer will get compared
                    arr[i] = left[j]
                    j+=1
                else:
                    arr[i] = right[k]
                    k+=1
                i+=1
            while j < len(left):
                arr[i] = left[j]  # need to pass an integer (not a slice list) bec i'm comparing on line 9
                j+=1
                i+=1
            while k < len(right):
                arr[i] = right[k]  # same,pass the integer, not the slice of the whole end of the list
                k+=1
                i+=1

        
        def mergeSort(arr, l, r):
            if l == r:
                return arr

            else:
                m = (l + r) // 2
                mergeSort(arr, l, m)
                mergeSort(arr, m+1, r)

                merge(arr, l, m, r)

        
        mergeSort(nums, 0, len(nums)-1)
        return nums


# in tihs solution, left and right are represented intervals because we have pointers at indices
# this means you're not making a deep copy at every level when you slice
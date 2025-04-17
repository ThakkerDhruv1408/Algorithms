from typing import List

class Solution:

    def insertionSort(self, nums: List[int]) -> List[int]:       # T = O(n²) & S = O(1)
        
        for i in range(1, len(nums)):

            key = nums[i]
            j = i - 1

            while j >= 0 and nums[j] > key:

                nums[j+1] = nums[j]
                j -= 1

            nums[j+1] = key

        return nums


    def insertionSort2(self, nums: List[int]) -> List[int]:          # T = O(n²) & S = O(1)

        for i in range(1,len(nums)):

            j = i
            while j > 0 and nums[j] < nums[j-1]:

                nums[j], nums[j-1] = nums[j-1], nums[j]
                j-= 1
        
        return nums
    
# Testing

n = [1,4,7,8,5,2,3,6,9,0]
test = Solution()
w = test.insertionSort2(n)
print(w)
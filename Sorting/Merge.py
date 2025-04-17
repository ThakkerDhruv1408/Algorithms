from typing import List

class Solution:

    def mergeSort(self, nums: List[int]) -> List[int]:      # T = O(n log(n))

        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])

        return self.merge(left, right)


    def merge(self, left: List[int], right:List [int]) -> List[int]:

        i, j = 0, 0

        result = []
        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
            
        result.extend(left[i:])
        result.extend(right[j:])

        return result
    
# Testing

n = [1,3,5,7,9,8,6,4,2,0] 
test = Solution()
w = test.mergeSort(n)
print(w)


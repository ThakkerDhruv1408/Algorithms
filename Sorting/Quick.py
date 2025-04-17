from typing import List

class Solution:

    def quickSort(self, nums: List[int]) -> List[int]:      # T = O(n^2) | Avg. T = O(n log(n))

        if len(nums) <= 1:
            return nums
        
        pivot = nums[0]

        left =  [x for x in nums[1:] if x <= pivot]
        right = [x for x in nums[1:] if x > pivot]

        return self.quickSort(left) + [pivot] + self.quickSort(right)
    
# Testing

test = Solution()
n = [1,2,5,4,7,8,9,6,3]
w = test.quickSort(n)
print(w)
from typing import List

class Solution:

    def selectionSort(self, nums: List[int]) -> List[int]:      # T = O(n²) S = O(1)
        n = len(nums)
        for i in range(n-1):
            smallest_idx = i
            for j in range(i+1, n):

                if nums[j] < nums[smallest_idx]:
                    smallest_idx = j
                
            nums[i], nums[smallest_idx] = nums[smallest_idx], nums[i]
            
        return nums


    def smallest_index(self, nums: List[int], start: int) -> int:           # T = O(n) S = O(1)
        
        smallest, smallest_idx = nums[start] , start

        for i in range(start+1, len(nums)):

            if nums[i] < smallest:

                smallest = nums[i]
                smallest_idx = i

        return smallest_idx


    
    def selectionSort2(self, nums: List[int]) -> List[int]:     # T = O(n²) S = O(n)

        for i in range(len(nums)-1):
            smallest = self.smallest_index(nums, i)
            nums[i], nums[smallest] = nums[smallest], nums[i]
        return nums

n = [1,4,7,8,5,2,0,3,6,9]
test = Solution()
x = test.selectionSort(n)
print(x)
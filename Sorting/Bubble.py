from typing import List

class Solution:
    def bubbleSort(self, nums: List[int]) -> List[int]:     # T = O(n²) & S = O(1)      Best Case = O(n²)
        n, count = len(nums), 0
        for i in range(n - 1):

            count += 1
            for j in range(n - i -1):

                if nums[j+1] < nums[j]:
                    
                    nums[j], nums[j+1] = nums[j+1] , nums[j]
                    # print(nums, count)

        return nums, count


    def bubbleSort2(self, nums: List[int]) -> List[int]:    # T = O(n²) & S = O(1)      Best Case = O(n) "Array is already sorted!"
        
        n = len(nums)
        count = 0
        for i in range(n-1):

            bool = False
            count += 1
            for j in range(n - i - 1):

                if nums[j+1] < nums[j]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    bool = True
                    # print(nums, count)
            
            if bool == False:
                return nums, count
        
        return nums, count
        

# Testing

test = Solution()
# nums = [-11,-9,-7,-5,1,5,4,7,8,9,8,7,4,5,6,3,25,4,1,2,5,6]
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
w, x = test.bubbleSort2(nums)
print(w, x)
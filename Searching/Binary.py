from typing import List

class Solution:

    def binarySearch(self,nums: List[int], target: int, left=0, right=None)-> int:      # T = O(log(n)) & S = O(1)

        if right is None:
            right = len(nums) - 1


        while left <= right:

            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return -1


    
    def binarySearch2(self,nums: List[int], target: int, left=0, right=None)-> int:     # T = O(log(n)) & S = O(log(n))

        if right is None:
            right = len(nums) - 1
        
        if left > right:
            return -1
        
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        
        if nums[mid] < target:
            return self.binarySearch2(nums, target, mid+1, right)
        
        else:
            return self.binarySearch2(nums, target, left, mid-1)
        
        

# Testing

test = Solution()
nums = [0,1,2,3,4,5,6,7,8,9,10,40,50,60,70,80,1111,7777]
w = test.binarySearch(nums , 7)
print(w)
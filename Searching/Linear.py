from typing import List

class Solution:
    def linearSearch(self, nums: List[int], target: int) -> int:        # T = O(n) & S = O(1)

        for i in range(len(nums)):

            if nums[i] == target:
                return f"{target}: Value found on index {i}"
            
        return f"ValueError : {target} is not present in the list"
    
    
    def linearSearch2(self, nums: List[int], target: int) -> int:       # T = O(n) & S = O(1)
        
        for idx, val in enumerate(nums):
            
            if val == target:
                return f"{target}: Value found on index {idx}"
        
        return f"ValueError : {target} is not present in the list"

    
    def linearSearch3(self, nums: List[int], target: int) -> int:       # T = O(n²) & S = O(1)
        
        for num in nums:
            
            if num == target:
                return f"{target}: Value found on index {nums.index(num)}"
        
        return f"ValueError : {target} is not present in the list"


# Testing

test = Solution()
nums = [1,4,7,8,5,2,0,3,6,9]
w = test.linearSearch1(nums , 5)
print(w)
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        insert_pos = 0

        # First pass: Move all non-zero elements to the beginning
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_pos] = nums[i]
                insert_pos += 1

        # Second pass: Fill the remaining positions with zeros
        for i in range(insert_pos, len(nums)):
            nums[i] = 0
    
nums = [0,1,2,0,3]
sol = Solution()
sol.moveZeroes(nums)
print(nums)  # Output: [1, 2, 3, 0, 0]
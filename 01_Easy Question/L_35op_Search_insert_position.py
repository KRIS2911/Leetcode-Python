from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i=0
        while(i<len(nums) and target >= nums[i]):
            if(nums[i] == target):
                return i
            i += 1
        return i
    
sol=Solution()
print(sol.searchInsert([1,2,5,6],4))
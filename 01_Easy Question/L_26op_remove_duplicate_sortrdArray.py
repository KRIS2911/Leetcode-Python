from typing import List
class Solution:
    def removeDuplicatesortedArray(self,nums:List[int]) -> int:
        i = 0
        while(i<len(nums)):
            j=i+1
            while(j<len(nums) and nums[i]==nums[j]):
                nums.pop(j)
            i=j
        return nums
        
sol=Solution()
print(sol.removeDuplicatesortedArray([1,1,2,2,2,3]))
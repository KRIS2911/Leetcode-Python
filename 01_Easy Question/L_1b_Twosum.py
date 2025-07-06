from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j] == target):
                    return[i,j]
                


nums = [2, 7, 5, 9]
target = 9
sol = Solution()
result = sol.twoSum(nums, target)
print(result)
# from typing import List
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         i=0
#         while(i<len(nums)):
#             if(nums[i] == val):
#                 nums.pop(i)
#             else:
#                 i += 1
#         # print(nums)
#         return len(nums)
        
                
# s=Solution()
# print(s.removeElement([1,2,2,3],3))
# # print(s.removeElement())
            
            
            

from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        while(i<len(nums)):
            if(nums[i] == val):
                nums[i],nums[-1]=nums[-1],nums[i]
                nums.pop()
            else:
                i += 1
        print(nums)
        return len(nums)
        
                
s=Solution()
print(s.removeElement([1,2,2,3],2))
# print(s.removeElement())
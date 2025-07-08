from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=""
        for i in strs:
            if(len(i)<len(prefix) or prefix == ""):
                prefix=i
        need=len(strs)
        count=0
        result=""
        while(need != count):
            count=0
            for i in strs:
                if(prefix == i[:len(prefix)]):
                    count+=1
                result=prefix
                prefix=prefix[:-1]
        if(need == count):
            return result
        else:
            return ""
s=Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))



# # from typing import List

# # class Solution:
# #     def longestCommonPrefix(self, strs: List[str]) -> str:
# #         if not strs:
# #             return ""
# #         prefix = strs[0]
# #         for s in strs[1:]:
# #             while not s.startswith(prefix):
# #                 prefix = prefix[:-1]
# #                 if not prefix:
# #                     return ""
# #         return prefix

# # s = Solution()
# # print(s.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
            
        
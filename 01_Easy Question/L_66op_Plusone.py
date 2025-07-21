from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # s=digits[-1] + 1
        # digits[-1]=s
        # return list(digits) ## it is working but  not for all cases.
        
        s = int(''.join([str(i) for i in digits]))
        s += 1
        result=list(str(s))
        return [int(i) for i in result]

sol=Solution()
print(sol.plusOne([0,1,2,32]))
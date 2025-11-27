import math
class Solution:
    def reversedInt(self,x: int)->int:
        if x>0:
            val=int(str(x)[::-1])
        else:
            val=-(int(str(abs(x))[::-1]))
        
        if val<=-2**31 or val>=2**31+1:
            return 0
        else:
            return val
        
s=Solution()
print(s.reversedInt(123))
print(s.reversedInt(-456))
print(s.reversedInt(1534254623526))
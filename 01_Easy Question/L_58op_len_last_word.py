class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        Lst=s.split()
        if(len(Lst) == 0):
            return 0
        return(len(Lst[-1]))


sol=Solution()
print(sol.lengthOfLastWord("Hello World"))

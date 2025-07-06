class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0 or (x%10==0 and x!=0)):
            return False
        
        rev=0
        while(x>rev):
            last_dig=x%10
            rev=rev*10+last_dig
            x=x//10
        
        if(x==rev or x==rev//10):
            return True
        return False

sol=Solution()
print(sol.isPalindrome(121))
print(sol.isPalindrome(-121))
print(sol.isPalindrome(12215))       
print(sol.isPalindrome(1000)) 
print(sol.isPalindrome(45854))
print(sol.isPalindrome(4454))
 
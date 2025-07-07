class Solution:
    def romanToint(self,s:str)->int:
        translations={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        
        
        numbers=0
        s=s.replace("IV","IIII")
        s=s.replace("IX","VIIII")
        s=s.replace("XL","XXXX")
        s=s.replace("XC","LXXXX")
        s=s.replace("CD","CCCC")
        s=s.replace("CM","DCCCC")
        
        for char in s:
            numbers += translations[char]
        return numbers
sol=Solution()
print(sol.romanToint("IV"))





#### Best optimal way
# class Solution:
#     def romanToInt(self, s):
#         roman = {
#             'I': 1, 'V': 5, 'X': 10, 'L': 50,
#             'C': 100, 'D': 500, 'M': 1000
#         }
#         total = 0
#         prev = 0

#         for c in reversed(s):
#             curr = roman[c]
#             if curr < prev:
#                 total -= curr
#             else:
#                 total += curr
#             prev = curr

#         return total
    
# sol=Solution()
# print(sol.romanToInt("IV"))  

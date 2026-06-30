##Leetcode Problem 13 -> Roman to Integer

class Solution:
    def romantoInt(self, s):
        roman=s
        n=0
        d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for i in range(len(roman)):
            if i+1<len(roman) and d[roman[i]]<d[roman[i+1]]:
                n-=d[roman[i]]
            else:
                n+=d[roman[i]]
        return n

s=Solution()

#Testcase:

print(s.romantoInt("III")) #1

print(s.romantoInt("LVIII")) #2

print(s.romantoInt("MCMXCIV")) #3

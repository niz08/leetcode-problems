##Problem 9: Palindrome

class Solution:
    
    def Palindrome(self, x):
        
        a=str(x)
        
        if a == a[::-1]:
            
            return True
        
        else:
            
            return False

s=Solution()

s.Palindrome(121) #Test Case 1

s.Palindrome(-121) #Test Case 2

s.Palindrome(10) #Test Case 3

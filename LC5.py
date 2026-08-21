#LeetCode 5. Longest Palindromic Substring

class Solution(object):
    def longestPalindrome(self, s):
        start, end = 0,0
        def expand(x,y):
            while x>=0 and y<len(s) and s[x]==s[y]:
                x-=1
                y+=1
            return x+1, y-1
        for i in range(len(s)):
            l1,r1=expand(i,i)
            if r1-l1>end-start:
                start, end = l1,r1
            l2,r2 = expand(i, i+1)
            if r2-l2 > end-start:
                start, end = l2,r2
        return s[start:end +1]

s=Solution()

#TestCase 1:
print(s.longestPalindrome("babad"))
#TestCase 2:
print(s.longestPalindrome("cbbd"))

#LeetCode 69. Sqrt(x) [Binary Search]

class Solution(object):
    def mySqrt(self, x):
        if x < 2:
            return x
        t,y = 1, x//2
        while t<=y:
            mid=(t+y)//2
            if mid*mid==x:
                return mid
            elif mid*mid < x:
                t=mid+1
            else:
                y=mid-1
        return y

s=Solution()
#TestCase 1:
print(s.mySqrt(4))
#TestCase 2:
print(s.mySqrt(8))


##2 Sum Problem
# Main Concept Used: Hash Map/Dictionary

class Solution:
    def twoSum(l,target):
        d={}
        for i, j in enumerate(l):
            c=target-j
            if c in d:
                return d[c],i
            d[j]=i
s=Solution
print(s.twoSum([2,7,11,15],9))
print(s.twoSum([3,2,4],6))
print(s.twoSum([3,3],6))


        
        

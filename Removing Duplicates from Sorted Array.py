#LeetCode Problem 26 - Removing Duplicates from Sorted Array

class Solution(object):
    def removeDuplicates(self, nums):
        k=1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k]=nums[i]
                k+=1
        return k

s=Solution()

#TestCase 1:

print(s.removeDuplicates([1,1,2]))

#TestCase 2:

print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

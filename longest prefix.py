#LeetCode 14. Longest Common Prefix

class Solution(object):
    def longestCommonPrefix(self, strs):
        s=""
        for i in range(len(strs[0])):
            for j in strs:
                if j[i] == len(strs[0]) or j[i] != strs[0][i]:
                    return s
                    break
            s += strs[0][i]

s=Solution()

#TestCase 1:

print(s.longestCommonPrefix(["flow","flower","flight"]))

#TestCase 2:

print(s.longestCommonPrefix(["dog","racecar","car"]))

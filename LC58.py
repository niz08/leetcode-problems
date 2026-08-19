#LeetCode 58. Length of Last Word

class Solution(object):
    def lengthOfLastWord(self, s):
        a=s.split()
        return len(a[-1])

s=Solution()

#TestCase 1
print(s.lengthOfLastWord("Hello World"))
#TestCase 2
print(s.lengthOfLastWord("   fly me   to   the moon  "))
#TestCase 3
print(s.lengthOfLastWord("luffy is still joyboy"))

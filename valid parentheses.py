#LeetCode 20. Valid Parentheses

class Solution(object):
    def isValid(self, s):
        l=[]
        for i in range(len(s)):
            if s[i] in "({[":
                l.append(s[i])
            else:
                if l == []:
                    return False
                top=l.pop()
                if s[i] == ")" and top != "(":
                    return False
                if s[i] == "]" and top != "[":
                    return False
                if s[i] == "}" and top != "{":
                    return False
        return len(l) == 0

s=Solution()

#TestCase 1:
print(s.isValid("()"))
#TestCase 2:
print(s.isValid("()[]{}"))
#TestCase 3:
print(s.isValid("(]"))
#TestCase 4:
print(s.isValid("([])"))
#TestCase 5:
print(s.isValid("([)]"))

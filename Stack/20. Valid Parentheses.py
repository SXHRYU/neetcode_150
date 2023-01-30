import collections

class Solution:
    def isValid(self, s: str) -> bool:
        corresponding_brackets = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        res = []
        for char in s:
            if char == "(" or char == "[" or char == "{":
                res.append(char)
            else:
                if len(res) == 0 or res[-1] != corresponding_brackets[char]:
                    return False
                else:
                    res.pop()
        return res == []
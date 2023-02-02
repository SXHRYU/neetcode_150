from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = defaultdict(int)
        for char_s, char_t in zip(s, t):
            seen[char_s] += 1
            seen[char_t] -= 1
        for value in seen.values():
            if value != 0:
                return False
        return True

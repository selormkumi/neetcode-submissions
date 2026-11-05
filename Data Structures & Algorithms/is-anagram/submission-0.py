class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       # from collections import counter,
       return sorted(s) == sorted(t)

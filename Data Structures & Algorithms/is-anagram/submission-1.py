class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set1 = sorted(list(s))
        set2 = sorted(list(t))

        if set1 == set2:
            return True
        else:
            return False
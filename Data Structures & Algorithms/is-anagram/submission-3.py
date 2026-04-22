class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashset_s = {}
        hashset_t = {}

        letter_s = list(s)
        letter_t = list(t)

        for letter in letter_s:
            hashset_s[letter] = hashset_s.get(letter, 0) + 1
        
        for letter in letter_t:
            hashset_t[letter] = hashset_t.get(letter, 0) + 1

        return hashset_s == hashset_t
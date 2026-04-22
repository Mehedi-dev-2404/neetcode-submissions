class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for s in strs:
            key = "".join(sorted(s))

            if key in anagram_map:
                anagram_map[key].append(s)
            else:
                anagram_map[key] = [s]
        
        return list(anagram_map.values())
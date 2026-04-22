class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []

        for s in strs:
            found = False

            for group in groups:
                if sorted(s) == sorted(group[0]):
                    group.append(s)
                    found = True
                    break
            if not found:
                groups.append([s])
            
        return groups
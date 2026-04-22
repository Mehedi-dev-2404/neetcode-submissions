class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. Create an empty dictionary to store our groups
    # The key will be the sorted string, the value will be a list of words.
        groups = {}

        for word in strs:
            # 2. Sort the letters of the word so anagrams look identical
            # 'cat' -> ['a', 'c', 't'] -> 'act'
            sorted_word = "".join(sorted(word))
            # 3. If this 'id' isn't in our dictionary, create a new list for it
            if sorted_word not in groups:
                groups[sorted_word] = []
                
            # 4. Add the ORIGINAL word to the matching group
            groups[sorted_word].append(word)

        # 5. Return just the lists of words from our dictionary
        return list(groups.values())
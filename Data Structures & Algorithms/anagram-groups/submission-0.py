class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = {}

        for string in strs:
            key = "".join(sorted(string))

            if key not in group_anagrams:
                group_anagrams[key] = [string]
            else:
                group_anagrams[key].append(string)

        return list(group_anagrams.values())
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}

        for string in strs:
            # sorts current string in strs
            sorted_string = ''.join(sorted(string))

            if sorted_string in anagram_dict:
                anagram_dict[sorted_string].append(string)
            else:
                anagram_dict[sorted_string] = [string]

        return list(anagram_dict.values())
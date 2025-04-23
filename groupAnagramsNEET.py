class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaList = defaultdict(list)

        for s in strs:
            sortedStrs = ''.join(sorted(s))
            anaList[sortedStrs].append(s)

        return list(anaList.values())
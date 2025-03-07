class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        h = 0

        for i in range(len(citations)):
            if citations[i] > 0:
                hCitations = citations[i]
                hPapers = len(citations)-i
                if hCitations <= hPapers:
                    h = max(h, hCitations)
                else:
                    h = max(h, hPapers)
            elif citations[i] == 0:
                continue
            else:
                break
        return h
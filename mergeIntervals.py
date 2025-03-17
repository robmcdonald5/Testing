class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        
        ranges = []
        start = intervals[0][0]
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            current = intervals[i]
            if current[0] <= end:
                end = max(end, current[1])
            else:
                ranges.append([start, end])
                start = current[0]
                end = current[1]
            
        ranges.append([start, end])

        return ranges
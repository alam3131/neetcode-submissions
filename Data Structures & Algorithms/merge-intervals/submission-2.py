class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # If intervals array is length of 1 then the intervals are not overlapping
        if len(intervals) == 1:
            return intervals

        # Sort the intervals array
        intervals.sort()

        result = []
        result.append(intervals[0])

        l, r = 0, 1 
        while r < len(intervals):
            if result[l][1] < intervals[r][0]: # Not overlapping
                result.append(intervals[r])
                l += 1
            else: # Overlapping
                result[l] = [result[l][0], max(result[l][1], intervals[r][1])]
            r += 1

        return result




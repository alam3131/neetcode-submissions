class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # If intervals array is length of 1 then the intervals are not overlapping
        if len(intervals) == 1:
            return intervals

        # intervals.sort by the first tuple element
        intervals.sort()

        result = [] # result.append to add to array
        result.append(intervals[0])

        l, r = 0, 1 # Initially l and r point to index 0 and 1 of intervals array
        # check to see if the first two intervals need to be merged, if so
        # then merge them and place the new interval into the result array. 
        while r < len(intervals):
            # is index 1 of l's array < index 0 of r's array
            # if not then the array is overlapping
            if result[l][1] < intervals[r][0]: # Not overlapping
                result.append(intervals[r])
                l += 1
            else: # Overlapping
                result[l] = [result[l][0], max(result[l][1], intervals[r][1])]
            r += 1

        # now the l pointer points to the last element in the result array
        # if merging is not needed then place the interval into the result array and increment the l pointer by one
        # continue checking until r pointer reaches the end of the intervals array
        # return result
        return result




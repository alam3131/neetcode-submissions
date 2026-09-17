"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # intervals = sorted(intervals, key=lambda x: x.start)
        # days = [intervals] # List of list to represent days

        # # Loop through initial list to look for conflicts, starting with a comparison between
        # # first element and all other elements
        # for day in range(len(days)):
        #     for i in range(len(days[day])):
        #         for j in range(i+1, len(days[day])-1):
        #             if intervals[i].end > intervals[j].start:
        #                 if day+1 < len(days):
        #                     days[day+1].append(intervals[j])
        #                 else:
        #                     days.append([intervals[j]])

        #                 days[day].pop(j)

        # return len(days)

        # If conflict then create a new list to store conflicted intervals
        
        # Loop through new list for conflicts, if conflict then create new list to store conflicted intervals
        
        # Repeat until no conflicts exist, then return the len of days

        # Optimal Solution
        # Time complexity: O(nlogn)
        # Space complexity: O(n)
        maxCount, count = 0, 0
        sPtr, ePtr = 0, 0

        start = []
        end = []

        for i in intervals:
            start.append(i.start)
            end.append(i.end)

        start = sorted(start)
        end = sorted(end)

        while sPtr < len(intervals):
            if start[sPtr] < end[ePtr]:
                sPtr += 1
                count += 1
            else:
                ePtr += 1
                count -= 1
            maxCount = max(count, maxCount)
        
        return maxCount
            


        
        
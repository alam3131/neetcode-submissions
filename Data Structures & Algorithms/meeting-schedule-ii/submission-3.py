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

        if not intervals:
            return 0

        # Sort intervals by start time
        intervals.sort(key=lambda x: x.start)

        # Each room is a list of meetings that don't overlap
        rooms = []

        for interval in intervals:
            placed = False
            # Try to place the meeting in an existing room
            for room in rooms:
                # If no overlap with the last meeting in the room
                if room[-1].end <= interval.start:
                    room.append(interval)
                    placed = True
                    break
            # If it overlaps with all existing rooms, add a new room
            if not placed:
                rooms.append([interval])

        return len(rooms)
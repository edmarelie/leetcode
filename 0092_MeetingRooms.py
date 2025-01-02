"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # intervals = [(0,30),(5,10),(15,20)]
        #
        #  prevEnd = 20
        #  * *
        #    * *  *  *
        #         *  *
        #  0 5 10 15 20 25 30
        if len(intervals) == 0:
            return True

        intervals.sort(key=lambda i: i.start)
        prevEnd = intervals[0].end

        for i in range(1, len(intervals)):
            if intervals[i].start < prevEnd:
                return False
            else:
                prevEnd = max(prevEnd, intervals[i].end)
        return True

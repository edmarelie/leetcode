"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # intervals = [(0,40),(5,10),(15,20)]
        #
        # *  *  *  *  *  *  *  *  *
        #    *  *
        #          *  *
        # 0  5  10 15 20 25 30 35 40 45 50

        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        '''
        s                *
        start = [0,  5,  15]
        e            *
        end   = [10, 20, 40]
        '''

        res, count = 0, 0
        s, e = 0, 0

        while s < len(start):
            # There's meeting overlap
            if start[s] < end[e]:
                count += 1
                s += 1
            # There's no meeting overlap and other meeting has completed
            else:
                count -= 1
                e += 1
            res = max(res, count)
        
        return res

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        intervals = [[1,2],[2,3],[3,4],[1,3]]

                    *---*
                    *-------*
                        *---*
                            *---*
                    1   2   3   4
        
        Approach:
        1. Sort intervals
           intervals = [[1,2],[1,3],[2,3],[3,4]]
        2. If overlap, we need to remove the one with bigger end:
           - [1,2], [1,3], we remove [1,3]
           - condition for overlap:
             if end of intervals[i] > start of intervals[i+1]
        3. Continue to next intervals 
        '''
        res = 0
        i = 0
        intervals.sort()

        while i < len(intervals)-1:
            # Case of overlap
            if intervals[i][1] > intervals[i+1][0]:
                res += 1
                if intervals[i][1] > intervals[i+1][1]:
                    intervals.remove(intervals[i])
                else:
                    intervals.remove(intervals[i+1])
            else:
                i += 1
        
        return res

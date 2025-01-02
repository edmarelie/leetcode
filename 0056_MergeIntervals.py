class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        intervals = [[1,3],[2,6],[8,10],[15,18]]

                    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
                    *---*
                      *-------*
                                  *---*
                                                     *--------*
        Approach:
        1. Sort intervals
        2. Append intervals[i=0] to res array
           - compare res[-1][1] to the intervals[i][0]
             - if res[-1][1] >= intervals[i][0] - overlap:
               merge res[-1] and intervals[i]
             - else:
               append intervals[i] to res
        3. return res
        '''
        intervals.sort()
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            lastEnd = res[-1][1]

            # Case of overlap interval
            if lastEnd >= intervals[i][0]:
                res[-1] = [
                    min(res[-1][0], intervals[i][0]),
                    max(lastEnd, intervals[i][1]),
                ]
            # Case of non-overlap interval
            else:
                res.append(intervals[i])
        
        return res

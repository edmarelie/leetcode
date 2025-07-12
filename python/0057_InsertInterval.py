class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
                      *
        intervals = [[1,3], [6,9]]
        newInterval = [2,5]

        *-------*
                            *-----------*
            #===========#
        
        +---------------+   *-----------*
        1   2   3   4   5   6   7   8   9

        Approach:
        1. Merge interval:
           - if newInterval[start] < interval[end]
           - newInterval[newStart, newEnd]
             - newStart = min(interval[start], newInterval[start])
             - newEnd = max(interval[end], newInterval[end])
        2. Continue to next interval
        '''
        res = []

        for i in range(len(intervals)):
            # Case 1: new interval comes before intervals
            #
            # newInterval   # #
            # intervals[i]      * * * *
            #               0 1 2 3 4 5
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            
            # Case 2: new interval comes after intervals
            #
            # newInterval           # #
            # intervals[i]    * * *
            #               0 1 2 3 4 5
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            # Case 3: Merge
            #
            # newInterval         # #
            # intervals[i]    * * *
            #               0 1 2 3 4 5
            else:
                newInterval = (
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                )
        
        res.append(newInterval)
        return res

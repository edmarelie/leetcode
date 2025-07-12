class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        '''
        intervals = [[1,3],[2,3],[3,7],[6,6]]
        queries = [2,3,1,7,6,8]

                        *-------*
                            *---*
                                *---------------*
                                            *
                    0   1   2   3   4   5   6   7   8
                        |   |   |           |   |   |
        Queries:        |   |   |           |   |   |
        2               |   |   |           |   |   |
        3               |       |           |   |   |
        1               |                   |   |   |
        7                                   |   |   |
        6                                   |       |
        8                                           |
        
        Approach:
        1. Sort the intervals
        2. Sort the queries -> need to keep the index order for result
           queries = [1,2,3,6,7,8]
        3. Loop through sorted queries
        4. Loop through intervals:
           - use minHeap to store length and its end index
           - pop element from minHeap if end index is less that queries index
        5. Store minimum length in dictionary (key: q, val: minimum length)
        6. Return res in the list
        '''

        intervals.sort()
        res = {}
        minHeap = []
        i = 0
        
        for q in sorted(queries):
            # Populate matching intervals
            while i < len(intervals) and intervals[i][0] <= q:
                s, e = intervals[i]
                heapq.heappush(minHeap, [e-s+1, e])
                i += 1
            
            # Check and pop invalid intervals
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            
            # Get the top of the minHeap to return minimum length
            res[q] = minHeap[0][0] if minHeap else -1
        
        return [res[q] for q in queries]

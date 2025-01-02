class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        Approach:
        1. Create minHeap to store pair of [dist, points]
        2. Return k closest points
        '''

        minHeap = []
        heapq.heapify(minHeap)

        for x, y in points:
            dist = x**2 + y**2
            heapq.heappush(minHeap, [dist, x, y])
        
        res = []
        while len(res) < k:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
        
        return res

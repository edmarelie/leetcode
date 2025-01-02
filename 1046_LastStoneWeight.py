class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            stone1, stone2 = heapq.heappop(maxHeap), heapq.heappop(maxHeap)
            newStone = stone1 - stone2

            if newStone < 0:
                heapq.heappush(maxHeap, newStone)
              
        return -maxHeap[0] if len(maxHeap) == 1 else 0

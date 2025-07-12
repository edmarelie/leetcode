class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        # Only stores k element in the self.heap
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # Add value to self.heap
        heapq.heappush(self.heap, val)

        # Maintains the self.heap to be the length of k
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        # Return top of the heap
        return self.heap[0]
        

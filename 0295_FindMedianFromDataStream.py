class MedianFinder:
    '''
    Approach:
    1. use minHeap and maxHeap
       
       minHeap - For top of the stack
       ----------------------------------
       maxHeap - For bottom of the stack

    2. Every added element need to be stored either in minHeap/maxHeap
       - Check whether the values if bigger than top of maxHeap:
         - if yes, store in minHeap
         - if no, store in maxHeap
       - Both heap need to be kept balance (difference in length should be <= 1)
    3. If both length of the heap is the same: return top of both heap divided by 2
       Otherwise, return the top of the longer heap
    '''

    def __init__(self):
        self.minHeap = [] # for top of the stack
        self.maxHeap = [] # for bottom of the stack

    def addNum(self, num: int) -> None:
        if self.maxHeap and num < -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)

        # Balance the heap
        if len(self.maxHeap) - len(self.minHeap) > 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        elif len(self.minHeap) - len(self.maxHeap) > 1:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))         

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        elif len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        else:
            return self.minHeap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

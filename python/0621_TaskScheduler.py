class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        tasks = ["A","A","A","B","C"]
        n = 3

        1    2    3    4       5    6       7       8       9
        A -> B -> C -> Idle -> A -> Idle -> Idle -> Idle -> A

        Approach:
        1. Store the most frequent task in maxHeap.
        2. Use queue to store the unavailable Task until it's available again
        '''

        taskCount = Counter(tasks)
        maxHeap = [-i for i in taskCount.values()]
        heapq.heapify(maxHeap)

        q = []
        time = 0

        while maxHeap or q:
            time += 1
            # Choose task with most count
            if maxHeap:
                freq = 1 + heapq.heappop(maxHeap)
                # Store unavailable task in queue
                if freq:
                    q.append([freq, time + n])
            
            # Put back available task in maxHeap
            while q and q[0][1] == time:
                heapq.heappush(maxHeap, q.pop(0)[0])
        
        return time

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // Create HashMap with occurrent of each element
        Map<Integer, Integer> count = new HashMap<>();
        for (int num : nums) {
            count.put(num, count.getOrDefault(num, 0)+1);
        }

        // Use MinHeap to sort most occurrence
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> a[0] - b[0]);

        // Iterate through HashMap
        for (Map.Entry<Integer, Integer> entry : count.entrySet()) {
            heap.offer(new int[] {entry.getValue(), entry.getKey()});
            if (heap.size() > k) {
                heap.poll();
            }
        }

        // Populate the result
        int [] res = new int[k];
        for (int i=0; i<k; i++) {
            res[i] = heap.poll()[1];
        }

        return res;
    }
}

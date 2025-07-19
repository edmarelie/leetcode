class Solution {
    public boolean hasDuplicate(int[] nums) {
        Map<Integer, Integer> hashDuplicate = new HashMap<>();

        for (int num : nums) {
            if (hashDuplicate.containsKey(num)) {
                return true;
            }
            hashDuplicate.put(num, hashDuplicate.getOrDefault(num, 0) + 1);
        }
        return false;
    }
}

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> hashCompl = new HashMap<>();

        for (int i=0; i<nums.length; i++) {
            int compl = target - nums[i];
            if (hashCompl.containsKey(compl)) {
                return new int[] { hashCompl.get(compl), i };
            }
            hashCompl.put(nums[i], i);
        }
        return new int[] {};
    }
}

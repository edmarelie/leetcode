class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> hashString = new HashMap<>();

        for (String subStr : strs) {
            char[] charArray = subStr.toCharArray();
            Arrays.sort(charArray);
            String sortedSubStr = new String(charArray);

            if (!hashString.containsKey(sortedSubStr)) {
                hashString.put(sortedSubStr, new ArrayList<>());
            }
            hashString.get(sortedSubStr).add(subStr);
        }
        return new ArrayList<>(hashString.values());
    }
}
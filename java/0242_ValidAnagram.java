class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        Map<Character, Integer> hashMapS = new HashMap<>();
        Map<Character, Integer> hashMapT = new HashMap<>();

        for (int i=0; i<s.length(); i++) {
            hashMapS.put(s.charAt(i), hashMapS.getOrDefault(s.charAt(i), 0) + 1);
            hashMapT.put(t.charAt(i), hashMapT.getOrDefault(t.charAt(i), 0) + 1);
        }

        return hashMapS.equals(hashMapT);
    }
}

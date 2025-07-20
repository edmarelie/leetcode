class Solution {

    public String encode(List<String> strs) {
        StringBuilder res = new StringBuilder();
        for (String str : strs) {
            res.append(str.length()).append("#").append(str);
        }
        return res.toString();
    }

    public List<String> decode(String str) {
        // Init res List
        List<String> res = new ArrayList<>();

        int i = 0;

        // Loop through the string
        while (i < str.length()) {
            int j = i;
            // Moves pointer j to '#'' to get the string length
            // Use single quote for char
            while (str.charAt(j) != '#') {
                j++;
            }

            // Gets length
            int length = Integer.parseInt(str.substring(i, j));
            // Moves pointer i to first letter
            i = j + 1;
            // Moves pointer j to last letter + 1
            j = i + length;
            // Stores substring to res.
            res.add(str.substring(i, j));
            i = j;
        }
        return res;
    }
}

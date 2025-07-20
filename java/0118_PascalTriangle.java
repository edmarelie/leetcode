class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> triangle = new ArrayList<>();

        if (numRows == 0) {
            return triangle;
        }

        List<Integer> firstRow = new ArrayList<>();
        firstRow.add(1);
        triangle.add(firstRow);

        for (int i=1; i<numRows; i++) {
            List<Integer> prevRow = triangle.get(i - 1);
            List<Integer> curRow = new ArrayList<>();

            // The first element of every row is 1
            curRow.add(1);

            // Calculate middle element
            for (int j=1; j<i; j++) {
                curRow.add(prevRow.get(j-1) + prevRow.get(j));
            }

            // The last element of every row is 1
            curRow.add(1);

            // Update result
            triangle.add(curRow);
        }
        return triangle;
    }
}
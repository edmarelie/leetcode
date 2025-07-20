class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<List<Integer>> triangle = new ArrayList<>();

        List<Integer> firstRow = new ArrayList<>();
        firstRow.add(1);
        triangle.add(firstRow);

        if (rowIndex==0) {
            return triangle.get(rowIndex);
        }

        for (int i=1; i<=rowIndex; i++) {
            List<Integer> prevRow = triangle.get(i-1);
            List<Integer> curRow = new ArrayList<>();

            // 1st element
            curRow.add(1);

            // Middle element
            for (int j=1; j<i; j++) {
                curRow.add(prevRow.get(j-1) + prevRow.get(j));
            }

            // Last element
            curRow.add(1);

            // Update triangle
            triangle.add(curRow);
        }
        return triangle.get(rowIndex);
    }
}
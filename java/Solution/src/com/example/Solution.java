package com.example;

import static java.lang.Character.isDigit;

public class Solution {
    public static int test(String a) {
        //              i
        //            j
        int result = 0;
        int i = 0;

        while ( i < a.length() ) {
            // Skip non-digit characters
            while (i < a.length() && !isDigit(a.charAt(i))) {
                i++;
            }

            // If we've reached the end of the string, break
            if (i == a.length()) {
                break;
            }

            // Found a digit, now find the end of the number
            int j = i;
            while (j < a.length() && isDigit(a.charAt(j))) {
                j++;
            }

            // Parse the number and add to result
            // This check is crucial if there are no digits after non-digits
            if (i < j) {
                int number = Integer.parseInt(a.substring(i, j));
                result += number;
            }
            i = j;
        }
        return result;
    }
}

class Solution:
    def maxScore(self, s: str) -> int:
        '''
             0 1 2 3 4 5
        s = "0 1 1 1 0 1"

        sumS = 4
        '''
        # Gets sumS
        sumS = 0
        for numS in s:
            sumS += int(numS)

        # Loop through the number to calculate maxVal
        maxVal = 0
        numOfZeros = 0

        for i in range(len(s)-1):
            if int(s[i]) == 0:
                numOfZeros += 1
            else:
                sumS -= 1
            maxVal = max(maxVal, numOfZeros + sumS)

        return maxVal

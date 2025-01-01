class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''                     h
                 0  1  2  3  4  5  6  7  8  9  10
                 l  i     r
                    *  *
            A = [1, 3, 5, 7]
                          j
                          *  *
            B = [2, 4, 6, 8, 9, 10,11,12]
        
                                m  m
        comb =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12]
        '''

        # Get the combination length and half to find the median position
        combLen = len(nums1) + len(nums2)
        half = combLen // 2

        # Need to make sure A is always shorter length
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A

        # Do binary search on both nums1 and nums2
        # nums1: mid value (i) = (l+r) // 2
        # nums2: mid value (j) = half - i - 2
        # We need to compare value of:
        # - A[i] 
        l, r = 0, len(A)-1

        while True:
            i = (l+r) // 2
            j = half - i - 2
            print('i, j:', i, j)

            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i+1] if i+1 < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j+1] if j+1 < len(B) else float("inf")

            # Partition found
            if Aleft <= Bright and Bleft <= Aright:
                if combLen % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    return min(Aright, Bright)

            elif Bleft > Aright:
                l = i + 1
        
            else: # Aleft > Bright
                r = i - 1

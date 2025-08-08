class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
                  l             r
        height = [1,7,2,5,4,7,3,6]

        Approach:
        1. Use 2 pointers
        2. Calculate the volume: (r-l) * min(height[l], height[r])
           - if height[l] <= height[r]: move l
           - if height[r] < height[l]: move r
        '''

        l = 0
        r = len(heights)-1
        maxVol = 0

        while l < r:
            vol = (r-l) * min(heights[l], heights[r])
            maxVol = max(maxVol, vol)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxVol

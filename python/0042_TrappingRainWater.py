class Solution:
    def trap(self, heights: List[int]) -> int:
        '''
                                l                 
                                r
        height = [0,2,0,3,1,0,1,3,2,1]

        Approach:
        1. If maxL > heights[l]:
           - maxL - heights[l]
        2. Moving l and r:
           - if heights[l] <= heights[r]:
             - move l
           - else:
             - move r
        '''
        l = 0
        r = len(heights)-1
        maxL = maxR = 0
        water = 0

        while l < r:
            if heights[l] <= heights[r]:
                maxL = max(maxL, heights[l])
                if maxL > heights[l]:
                    water += maxL - heights[l]
                l += 1

            else:
                maxR = max(maxR, heights[r])
                if maxR > heights[r]:
                    water += maxR - heights[r]
                r -= 1
        
        return water

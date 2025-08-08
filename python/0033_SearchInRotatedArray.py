class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
                l
                          r
                    m
                0 1 2 3 4 5
        nums = [3,4,5,6,1,2]
        '''

        l, r = 0, len(nums)-1

        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            
            # Left is sorted
            #             m
            # nums = [3,4,5,6,1,2]
            if nums[l] <= nums[m]:
                # Search right
                if (
                    nums[l] > target or # target = 1
                    nums[m] < target    # target = 6
                ):
                    l = m + 1

                # Search left
                else:
                    r = m - 1
            
            # Right is sorted
            #             m
            # nums = [6,1,2,3,4,5]
            else:
                # Search left
                if (
                    nums[r] < target or # target = 6
                    nums[m] > target    # target = 1
                ):
                    r = m - 1

                # Search right
                else:
                    l = m + 1

        # Not found
        return -1

            

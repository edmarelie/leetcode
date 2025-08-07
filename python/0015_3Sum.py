class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        nums = [-1,0,1,2,-1,-4]

                            i  j       k
        1. sort -> nums = [-1,-1,0,1,2,4]
        """
        # Sort the array
        nums.sort()
        res = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        return res
        

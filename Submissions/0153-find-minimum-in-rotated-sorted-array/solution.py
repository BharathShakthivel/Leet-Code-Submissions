class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Brute Force - Time - O(n), Space - O(1)
        # nums.sort()
        # return nums[0]
        
        # Min index Method 
        
        l,r = 0, len(nums)-1
        while l<r:
            m = (l+r)//2
            if nums[m]>nums[r]:
                l = m+1
            else:
                r = m

        if nums[0]<nums[r]:
            return nums[0]
        return nums[l] 

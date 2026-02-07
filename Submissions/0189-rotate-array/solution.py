class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Brute Force
        # n = len(nums)
        # for i in range(k):
        #     for j in range(n-1,0,-1):
        #         nums[j],nums[j-1] = nums[j-1],nums[j]
        
        # Optimal Solution
        k = k% len(nums)
        n = len(nums)
        def reverse_array(l,r):
            while l<r:
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
                r-=1

        reverse_array(0,n-1)
        reverse_array(0,k-1)
        reverse_array(k,n-1)


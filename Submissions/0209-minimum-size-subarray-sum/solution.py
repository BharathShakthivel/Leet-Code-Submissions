class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l = 0
        sum_val = 0
        min_length = len(nums)+1
        if not nums:
            return 0
        for r in range(len(nums)):
            sum_val += nums[r]
            while sum_val>=target:
                    min_length = min(min_length,r - l + 1)
                    sum_val -= nums[l]
                    l+=1
        if min_length == len(nums)+1:
            return 0
        return min_length
                

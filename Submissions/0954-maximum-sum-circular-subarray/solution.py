class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if not nums:
            return 0
        cur_max, max_sum = 0, float("-inf")
        cur_min, min_sum = 0, float("inf")
        total = 0
        n = len(nums)
        for i in range(n):
            cur_max+=nums[i]
            cur_max = max(cur_max, nums[i])
            max_sum = max(max_sum,cur_max)
            cur_min+=nums[i]
            cur_min = min(cur_min, nums[i])
            min_sum = min(min_sum,cur_min)
            total+=nums[i]


        return max(max_sum, (total - min_sum)) if max_sum > 0 else max_sum


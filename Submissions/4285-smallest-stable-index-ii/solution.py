class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefix_max = [float("-inf")] * n
        suffix_min = [float("inf")] * n
        prefix_max[0] = nums[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i-1], nums[i])
        
        suffix_min[n-1] = nums[n-1]
        for j in range(n-2, -1, -1):
            suffix_min[j] = min(suffix_min[j+1], nums[j])
        for l in range(n):
            stability_score = abs((prefix_max[l]) - (suffix_min[l]))
            if stability_score <=k:
                return l
        return -1

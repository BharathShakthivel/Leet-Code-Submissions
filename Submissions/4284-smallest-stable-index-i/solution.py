class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        l = 0
        n = len(nums)
        for i in range(n):
            max_num = max(nums[:i+1])
            min_num = min(nums[i:])
            stability_score = abs(max_num) - abs(min_num)
            if stability_score <=k:
                return i
        return -1

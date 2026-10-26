class Solution:
    def trap(self, height: List[int]) -> int:
        # Time and Space - O(n)
        total_sum = 0
        n = len(height)
        cur_max = 0
        prefix_max = [0] * n
        suffix_max = [0] * n
        for i in range(n):
            cur_max = max(cur_max,height[i])
            prefix_max[i] = cur_max
        cur_max = 0
        for j in range(n-1,-1,-1):
            cur_max = max(cur_max,height[j])
            suffix_max[j] = cur_max
        for k in range(n):
            cur_sum = min(prefix_max[k],suffix_max[k]) - height[k]
            if cur_sum > 0:
                total_sum+= cur_sum
        return total_sum

            


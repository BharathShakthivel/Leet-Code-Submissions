class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        nums.sort(reverse = True)
        n = len(nums)
        total = sum(nums)
        if total % k !=0:
            return False
        equal_part_value = total // k
        if nums[0] > equal_part_value:
            return False
        
        res = [0] * k
        def backtrack(i):
            if i == n:
                return True
            for j in range(k):
                if res[j] + nums[i] <= equal_part_value:
                    res[j]+=nums[i]
                    if backtrack(i+1):
                        return True
                    res[j]-= nums[i]
                    if res[j]==0:
                        break
            return False
        return backtrack(0)

            

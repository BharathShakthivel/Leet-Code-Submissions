class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        # FAILED CASES

        # left = 0
        # cur_sum = 0
        # min_sum = float("inf")
        # for right in range(len(nums)):
        #     cur_sum+=nums[right]
        #     while (right-left+1)>r:
        #             cur_sum-=nums[left]
        #             left+=1
        #     if l <= (right-left+1) and (right-left+1) <= r:
        #         if cur_sum > 0 :
        #             min_sum = min(min_sum,cur_sum)
        # return -1 if min_sum == float("inf") else min_sum
        
        
        # n =len(nums)
        # cur_sum = 0
        # min_sum = float("inf")
        # for i in range(n):
        #     for j in range(i,n):
        #         if l <= (j-i+1) and (j-i+1) <=r:
        #             cur_sum+=nums[j]
        #             if cur_sum>0:
        #                 min_sum = min(min_sum,cur_sum)
        # return -1 if min_sum == float("inf") else min_sum



        n = len(nums)
        min_sum = float("inf")
        for i in range(n):
            cur_sum = 0 
            for j in range(i,n):
                length = j - i + 1
                if length > r:
                    break
                cur_sum += nums[j]
                if l <= length <= r:
                    if cur_sum > 0:
                        min_sum = min(min_sum,cur_sum)
        return -1 if min_sum == float("inf") else min_sum

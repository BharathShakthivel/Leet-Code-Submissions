class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # # Brute Force - O(N2)
        # # Core Idea
        # # We select a number and add it with the rest to check if it match our target
        # # If so we will add it to our res count
        # res = 0
        # for i in range(len(nums)):
        #     sum = 0
        #     for j in range(i,len(nums)):
        #         sum+=nums[j]
        #         if sum == k:
        #             res+=1

        # return res

        # # Optimal Solution O(N)
        # # We use prefic sum Hash map to add the prefic sums
        # # We check if the difference between the current sum and the target exists in prefix sum, if so we add it to our result count - Because that many time we can chop the element within the subarray to get our target sum
        # # Final we keep updating the current prefix to our hashmap, we add by one if it already exists in the hash, else
        # # we keep it as zero.

        res = 0
        cur_sum = 0
        prefix_sum = {0:1} # This is a imaginardefault prefix sum that exists in the array.

        for n in nums:
            cur_sum+=n
            diff = cur_sum - k
            res+=prefix_sum.get(diff,0)
            prefix_sum[cur_sum] = 1 + prefix_sum.get(cur_sum,0)
        return res

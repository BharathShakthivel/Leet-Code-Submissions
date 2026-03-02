# Brute Force - O(N) * O(N) = O(N*2) - !0 Minutes
# import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        answer = [1] * n
        for i in range(1,n):
            prefix[i] = prefix[i-1] * nums[i-1]
        for j in range(n-2,-1,-1):
            suffix[j] = suffix[j+1] * nums[j+1]
        for k in range(n):
            answer[k] = prefix[k] * suffix[k]
        return answer

        # right_product = 1
        # for j in range(n-1,-1,-1):
        #     prefix[j] = prefix[j] * right_product
        #     right_product = right_product * nums[j]
        # return prefix
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # answer = []
        # for i in range(len(nums)):
        #     cur_prefix = nums[0:i]
        #     cur_suffix = nums[i+1:]
        #     answer.append(math.prod(cur_prefix)*math.prod(cur_suffix))
        # return answer
# Optimal Solution - Time - O(N) ; Space = O(N)

        # n = len(nums)
        # answer = [0] * n
        # prefix = [1] * n
        # suffix = [1] * n
        # for i in range(1,n):
        #     prefix[i] = nums[i-1] * prefix[i-1]
        # for j in range(n-2,-1,-1):    
        #     suffix[j] = nums[j+1] * suffix[j+1]
        # for k in range(n):
        #     answer[k] = prefix[k] * suffix[k]
        # return answer


# Most Optimal Solution - Time - O(N) ; Space = O(1)

        # n = len(nums)
        # prefix = [1] * n
        # for i in range(1,n):
        #     prefix[i] = nums[i-1] * prefix[i-1]
        # right_product = 1
        # for j in range(n-1,-1,-1):    
        #     prefix[j] = prefix[j] * right_product
        #     right_product*=nums[j]
        # return prefix

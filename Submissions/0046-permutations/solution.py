class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # sol,res = [],[]

        # # Iterative backtracking - NOT THE BEST SOLUTION
        # # Time - n! * n ; Space: n! * n
        # # For every iteration we pick the element from the list and backtrack the rest until it hits base case.
        # #  The base case is when the len of original list becomes zero we append a copy to our res
        # # We pop the last element from current solution and we insert back the element to corresponding iteration.

        # #  The ultimate idea is that once the element is picked it is automatically neglected in the next itwration.
        # def backtrack(nums):
        #     if len(nums) == 0:
        #         res.append(sol[:])
        #         return
            
        #     for j in range(len(nums)):
        #         sol.append(nums[j])
        #         element = nums.pop(j)
        #         backtrack(nums)
        #         sol.pop()
        #         nums.insert(j,element)
        # backtrack(nums)
        # return res


        # GREG SOLUTION - SIMPLIFIED BACKTRACKING
        sol,res = [],[]
        n = len(nums)
        def backtrack():
            if len(sol) == n:
                res.append(sol[:])
            for i in nums:
                if i not in sol:
                    sol.append(i)
                    backtrack()
                    sol.pop()
        backtrack()
        return res


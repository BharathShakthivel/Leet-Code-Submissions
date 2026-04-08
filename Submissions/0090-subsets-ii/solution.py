class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Optimal For Loop:
        '''
        # Sort to group duplicates. Use backtracking with a start index.
        # At each recursion, add current subset.
        # Loop from `start` to end and choose next element.
        # Skip duplicates at the same level using:
        #   if i > start and nums[i] == nums[i-1]: continue
        # This avoids generating duplicate subsets.
        # Recurse with i+1, then backtrack.
        
        Small Version
        # Sort first. Backtrack and build subsets.
        # Skip duplicates at same recursion level (i > start and same value).
        # Choose -> recurse -> backtrack.
        '''
        # nums.sort()
        # sol,res = [],[]
        # n = len(nums)
        # def backtrack(start):
        #     res.append(sol[:])
        #     for i in range(start,n):
        #         if i>start and nums[i] == nums[i-1]:
        #             continue
        #         sol.append(nums[i])
        #         backtrack(i+1)
        #         sol.pop()
        # backtrack(0)
        # return res

        'Time Complexity - O(n 2 pow(n)) ; Space:'
        # While Loop (Include, Exclude):
        nums.sort()
        sol,res = [],[]
        n = len(nums)
        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()    
            while i + 1 < n and nums[i] == nums[i+1]:
                    i+=1
            backtrack(i+1)
        backtrack(0)
        return res


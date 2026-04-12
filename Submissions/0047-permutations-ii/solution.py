class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # Time - n! factorial 
        '''
        Mental Model -
        for n in count:
            choose
            recurse
            undo



            try 1
            go deeper
            come back

            try 2
            go deeper
            come back
        '''
        
        res,sol = [],[]
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i,0)
        def backtrack():
            if len(sol) == len(nums):
                res.append(sol[:])
                return
            for n in count:
                if count[n] > 0:
                    sol.append(n)
                    count[n]-=1
                    backtrack()
                    count[n]+=1
                    sol.pop()
        backtrack()
        return res
        

                
                

        

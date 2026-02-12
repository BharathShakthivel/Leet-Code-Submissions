class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # FAILED ATTEMPT
        
        # nums.sort()
        # res = []
        # l,r = 0,len(nums)-1
        # while l<r and l+1 !=r-1:
        #         if nums[l] != nums[l+1] and nums[l] != nums[r] and nums[l]!= nums[r-1]:
        #             four_sum = nums[l] + nums[l+1] + nums[r] + nums[r-1]
        #             if four_sum>target:
        #                 r-=1
        #             elif four_sum<target:
        #                 l+=1
        #             else:
        #                 res.append([nums[l],nums[l+1],nums[r],nums[r-1]])
        #                 l+=1
        #                 r-=1         
        # return res
        
        # TWO POINTER - O(N3)
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                l,r = j+1,len(nums)-1
                while l<r:
                    four_sum = nums[i] + nums[j] + nums[l] + nums[r]
                    if four_sum > target:
                        r-=1
                    elif four_sum < target:
                        l+=1
                    else:
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        r-=1
                        while l<r and nums[l] == nums[l-1]:
                            l+=1
                        while r>l and nums[r] == nums[r+1]:
                            r-=1
        return res


        # MOST OPTIMAL - 2 POINTER TECHNIQUE WITH RECURRSION

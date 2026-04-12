class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#         prev_dict = {}
#         for i,n in enumerate(nums):
#             diff = target - n
#             if diff in prev_dict:
#                 return [prev_dict[diff],i]
#             prev_dict[n] = i
#         return

        # my_dict ={}
        # for i,v in enumerate(nums):
        #     diff = target - v
        #     if diff in my_dict:
        #         return [my_dict[diff],i]
        #     my_dict[v] = i    
        # return
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return i,j

























        # Binary Search Index Mismatch

        # nums.sort()
        # for i in range(len(nums)):

        #         diff = target - nums[i]
        #         l,r = i+1, len(nums)-1
        #         while l<=r:
        #             mid = (l+r)//2
        #             if nums[mid] > diff:
        #                 r = mid -1
        #             elif nums[mid] < diff:
        #                 l = mid +1
        #             else:
        #                 return i,mid

        # Optimal

        my_dict = {}
        for i,v in enumerate(nums):
            diff = target - v
            if diff in my_dict.keys():
                return [i,my_dict[diff]]
            my_dict[v] = i















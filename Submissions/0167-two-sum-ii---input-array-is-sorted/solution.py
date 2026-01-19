class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # my_dict = {}
        # for index,value in enumerate(numbers):
        #     diff = target - value
        #     if diff in my_dict:
        #         return [my_dict[diff]+1,index+1]
        #     my_dict[value] = index
        # return
        
        # Two Pointer approach
        
        # l = 0
        # r = len(numbers)-1
        # while l<r:
        #     if numbers[l] + numbers[r] == target:
        #         return [l+1,r+1]
        #     elif numbers[l] + numbers[r] > target:
        #         r-=1
        #     elif numbers[l] + numbers[r] < target:
        #         l+=1
        
        # return [l,r]

        # l = 0
        # r = len(numbers)-1
        # while l<r:
        #     if numbers[l] + numbers[r] > target:
        #         r-=1
        #     elif numbers[l] + numbers[r] < target:
        #         l+=1
        #     else: 
        #         return [l+1,r+1]
        # return [l,r]


        
        l = 0
        r = len(numbers)-1
        while l<r:
            curr_sum = numbers[l] + numbers[r]
            if  curr_sum > target:
                r-=1
            elif curr_sum < target:
                l+=1
            else: 
                return [l+1,r+1]
        return [l,r]

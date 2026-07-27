class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        Dutch National Flag Algorithm - Three pointer
        If 0 → swap with low, low++, mid++
        If 1 → mid++
        If 2 → swap with high, high--

        Here mid is looping from start till it crosses right pointer
        '''
        # l,r = 0, len(nums)-1
        # i = 0
        # def swap(i,j):
        #     temp = nums[i]
        #     nums[i] = nums[j]
        #     nums[j] = temp
        # while i<=r:
        #     if nums[i] == 0:
        #         swap(l,i)
        #         l+=1
        #     elif nums[i] == 2:
        #         swap(i,r)
        #         r-=1
        #         i-=1
        #     i+=1
        # return nums




















        l,r = 0, len(nums)-1
        i = 0
        def swap (a,b):
            temp = nums[a]
            nums[a] = nums [b]
            nums[b] = temp
        while i <=r:
            if nums[i]==0:
                swap(l,i)
                l+=1
            elif nums[i]==2:
                swap(r,i)
                r-=1
                i-=1
            i+=1
        return nums

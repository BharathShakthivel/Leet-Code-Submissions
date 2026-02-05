class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Brute Force O(N2)
        # res = 0
        # for i in range(len(height)):
        #     for j in range(i+1,len(height)):
        #         if height[i]<height[j]:
        #             cur_max = height[i] * (j-i)
        #         else:
        #             cur_max = height[j] * (j-i)
        #         if cur_max>res:
        #             res=cur_max
        # return res


        # Brute Force Simplified
        # res = 0
        # for i in range(len(height)):
        #     for j in range(i+1,len(height)):
        #         cur_max = min(height[i],height[j]) * (j-i)
        #         if cur_max>res:
        #             res=cur_max
        # return res

        # Optimal Solution

        # l,r = 0,len(height)-1
        # res = 0
        # while l<r:
        #      cur_max = min(height[l],height[r]) * (r-l)
        #      if cur_max>res:
        #         res=cur_max
        #      if height[l]<height[r]:
        #         l+=1
        #      else:
        #         r-=1
        # return res



















        res = 0
        l,r = 0,len(height)-1
        while l<r:
            cur_max = min(height[l],height[r]) * (r-l)
            if cur_max>res:
                res = cur_max
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return res
















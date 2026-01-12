class Solution:
    def mySqrt(self, x: int) -> int:
        # if x == 0:
        #     return 0
    
        # left = 1
        # right = x
    
        # while left <= right:
        #     mid = left + (right - left) // 2
        
        #     if mid == x // mid:
        #         return mid
        #     elif mid < x // mid:
        #         left = mid + 1
        #     else:
        #         right = mid - 1
    
    # When loop ends, right will be the floor of sqrt(x)
        # return right
        l = 0
        r = x
        res = 0
        while(l<=r):
            m = l + ((r-l)//2)
            if m ** 2 > x:
                r = m -1
            elif m ** 2 < x:
                l = m + 1
                res= m
            else:
                return m
        return res


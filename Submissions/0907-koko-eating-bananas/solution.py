class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        total = sum(piles)
        while l<r:
            mid = (l + r)//2
            cur_hour = 0
            for i in range(len(piles)):
                cur_hour+= ceil(piles[i]/mid)
            if cur_hour>h:
                l = mid + 1
            elif cur_hour<=h:
                r = mid
        return l



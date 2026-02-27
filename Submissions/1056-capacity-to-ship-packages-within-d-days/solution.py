class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r =sum(weights)
        valid_capacity = []
        while l<=r:
            mid = (l+r)//2
            cur_sum = 0
            cur_day = 1
            for i in range(len(weights)):
                if cur_sum + weights[i]>mid:
                    cur_day+=1
                    cur_sum = weights[i]
                else:
                    cur_sum+=weights[i]
            if cur_day>days:
                l = mid+1
            elif cur_day<=days:
                r = mid-1
                valid_capacity.append(mid)
        return min(valid_capacity)


        #Optimised Version 
        # We know that once we shrink the weights, the minimum would be left pointer value that corresponds to minimum capacity of the ship to load all the goods in order in d days.
        l = max(weights)
        r =sum(weights)
        while l<=r:
            mid = (l+r)//2
            cur_sum = 0
            cur_day = 1
            for i in range(len(weights)):
                if cur_sum + weights[i]>mid:
                    cur_day+=1
                    cur_sum = weights[i]
                else:
                    cur_sum+=weights[i]
            if cur_day>days:
                l = mid+1
            elif cur_day<=days:
                r = mid
        return l
        



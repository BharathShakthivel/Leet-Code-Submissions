class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Failed Approach
        
        # people.sort()
        # boats = set()
        # bout_count = set()
        # for i in range(len(people)):
        #     if people[i] < limit:
        #         if sum(boats)+people[i]<= limit:
        #             boats.add(people[i])
        #             if sum(boats) == limit:  
        #                 bout_count.add(tuple(boats))
        #                 boats = set()
        #             else:
        #                 continue
        #         elif sum(boats)+people[i]<= limit:
        #             bout_count.add(tuple(boats))
        #             boats = set()
        #             boats.add(people[i])
        # return len(bout_count)


        # Two Pointer Approach with Guidance:
        # people.sort()
        # boat_count = 0    
        # l,r = 0, len(people)-1
        # while l<=r:
        #     if people[l] + people[r] <= limit:
        #         boat_count+=1
        #         l+=1
        #         r-=1
        #     else:
        #         r-=1
        #         boat_count+=1
        # return boat_count

        # Two Pointer Apprach with less code 

        people.sort()
        boat_count = 0
        l,r = 0, len(people)-1
        while l<=r:
            remain = limit - people[r]
            boat_count+=1
            r-=1
            if l<=r and remain>= people[l]:
                l+=1
        return boat_count
            
    

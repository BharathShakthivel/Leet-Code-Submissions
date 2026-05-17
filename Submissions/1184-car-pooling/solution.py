class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Brute Force = O(n)
        trip_space = [0] * 1001
        for trip in trips:
            passenger,start,end = trip
            trip_space[start]+=passenger
            trip_space[end]-=passenger
        cur_pass= 0
        for i in range(1001):
            cur_pass+=trip_space[i]
            if cur_pass > capacity:
                return False
        return True
        # Time- n logn
        # trip_heap = []
        # for trip in trips:
        #     heapq.heappush(trip_heap,[trip[1],1,trip[0]])
        #     heapq.heappush(trip_heap,[trip[2],0,trip[0]])
        # while trip_heap:
        #     cur_trip_point,cur_type,cur_capacity = heapq.heappop(trip_heap)
        #     if cur_type == 0:
        #         capacity+= cur_capacity
        #     else:
        #         capacity-= cur_capacity
        #     if capacity <0:
        #         return False
        # return True

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        Your version vs Neetcode version (core difference)
        
        Your version:
        time += 1
        release from queue
        execute task
        push with counter + n + 1
        
        Neetcode version:
        time += 1
        execute task
        push with time + n
        release from queue
        
        So:
        You release BEFORE executing
        Neetcode releases AFTER executing
        That shifts the cooldown by one unit, which is why you need +1.
        '''
        
        # Own Method -  Time O(n)
        # from collections import deque
        # max_heap = []
        # freq_dict = {}
        # counter = 0
        # for i in tasks:
        #     freq_dict[i] = 1 + freq_dict.get(i,0)
        # for j in freq_dict.values():
        #     heapq.heappush(max_heap,-j)
        # heapq.heapify(max_heap)
        # q = deque()
        # while max_heap or q:
        #     counter+=1
        #     while q and q[0][1] <= counter:
        #             heapq.heappush(max_heap,q.popleft()[0])
        #     if max_heap:
        #         cur = 1 +heapq.heappop(max_heap)
        #         if cur:
        #             q.append((cur,counter+n+1))
        # return counter

        # Neetcode MEthod:
        # from collections import deque
        # Count = Counter(tasks)
        # max_heap = [-s for s in Count.values()]
        # heapq.heapify(max_heap)
        # q = deque()
        # time = 0
        # while max_heap or q:
        #     time+=1
        #     if max_heap:
        #         cur = 1 + heapq.heappop(max_heap)
        #         if cur:
        #             q.append([cur,time+n])
        #     if q and q[0][1] == time:
        #         heapq.heappush(max_heap,q.popleft()[0])
        # return time

        # Own Method but excuteing in Neetcode style:
        from collections import deque
        max_heap = []
        freq_dict = {}
        counter = 0
        for i in tasks:
            freq_dict[i] = 1 + freq_dict.get(i,0)
        for j in freq_dict.values():
            heapq.heappush(max_heap,-j)
        heapq.heapify(max_heap)
        q = deque()
        while max_heap or q:
            counter+=1
            if max_heap:
                cur = 1 +heapq.heappop(max_heap)
                if cur:
                    q.append((cur,counter+n))
            if q and q[0][1] == counter:
                    heapq.heappush(max_heap,q.popleft()[0])
        return counter
    

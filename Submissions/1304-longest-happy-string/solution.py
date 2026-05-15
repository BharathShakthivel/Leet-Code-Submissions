class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        #  Failed Approach
        
        # if (a ==1 and  b ==1 and c == 1):
        #     return 'abc'
        # max_heap = [[-a , 'a'],[-b , 'b'],[-c , 'c']]
        # heapq.heapify(max_heap)
        # res = ""
        # prev = None

        # while max_heap or prev:
        #     if prev and not max_heap:
        #         return ""
        #     count, char = heapq.heappop(max_heap)
        #     if len(res) <2:
        #         res+=char
        #         count+=1
        #     if len(res) >= 2 and (res[-1] != char and res[-2] != char):
        #         res+=char
        #         count+=1
        #     if prev:
        #         heapq.heappush(max_heap,prev)
        #         prev = None
        #     if count!=0:
        #         prev = [count,char]
        # return res

        #  Neet code:
        res,max_heap = "",[]
        for count, char in [[-a , 'a'],[-b , 'b'],[-c , 'c']]:
            if count!=0:
                heapq.heappush(max_heap,[count,char])
        while max_heap:
            count, char = heapq.heappop(max_heap)
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not max_heap:
                    break
                count_2,char_2 = heapq.heappop(max_heap)
                res+=char_2
                count_2+=1
                if count_2 !=0:
                    heapq.heappush(max_heap,[count_2,char_2])
            else:
                res+=char
                count+=1
            if count!=0:
                heapq.heappush(max_heap,[count,char])       
        return res


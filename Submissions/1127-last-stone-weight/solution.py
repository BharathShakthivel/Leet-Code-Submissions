class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Brute Force Time complexity: O(n^2 log n); Space - O(1) or O(n) - Depends on sorting algo
        # while len(stones) > 1:
        #     stones.sort()
        #     cur = stones.pop() - stones.pop()
        #     if cur:
        #         stones.append(cur)
        # if stones:
        #     return stones[0]
        # return 0
        # Using heap - Time complexity: O(n log n); Space - O(1)

        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            cur = abs(heapq.heappop(stones) - heapq.heappop(stones))
            if cur:
                heapq.heappush(stones,-cur)
        if stones:
            return -stones[0]
        return 0

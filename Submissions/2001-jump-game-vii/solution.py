class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # n = len(s)
        # start = 0
        # while (start <= n-1):
        #     for i in range((start+minJump),(start+maxJump +1)):
        #         if i<=n-1 and s[i] == '0':
        #             start = i
        #         else:
        #             return False
        # return start == n-1
        from collections import deque
        q = deque([0])
        n = len(s)
        farthest = 0
        while q:
            cur_index = q.popleft()
            start = max(cur_index+minJump, farthest +1)
            stop = cur_index+maxJump+1
            for i in range(start, min(stop,n)):
                if s[i] == '0':
                    q.append(i)
                    if i == n-1:
                        return True
            farthest = stop -1
        return False





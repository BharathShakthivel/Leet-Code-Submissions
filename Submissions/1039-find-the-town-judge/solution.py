class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # The problem is asking for a "judge" in a directed graph of trust relationships.
        # Think of each person as a node.
        # A directed edge u -> v means: u trusts v.

        # A judge must satisfy TWO conditions:
        # 1. Everyone else trusts the judge:
        #    → indegree == n - 1
        # 2. The judge trusts nobody:
        #    → outdegree == 0

        # Strategy:
        # - Build indegree map: counts how many people trust each person
        # - Build outdegree map: counts how many people each person trusts
        # - Then scan all people from 1 to n and find who satisfies both conditions

        # Edge case:
        # - If n == 1, that single person is trivially the judge
        #   (no one else exists, so both conditions are automatically satisfied)
        # if n ==1:
        #     return 1
        # indegree = {}
        # outdegree = {}
        # for u,v in trust:
        #     indegree[v] = 1 + indegree.get(v,0)
        #     outdegree[u]= 1 + outdegree.get(u,0)
        # for i in range(1,n+1):
        #     if indegree.get(i,0) == (n-1) and (i not in outdegree):
        #         return i
        # return -1
        
        #  Default Dict Method
        # if n ==1:
        #     return 1
        # from collections import defaultdict
        # incoming = defaultdict(int)
        # outgoing = defaultdict(int)
        # for src,dist in trust:
        #     incoming[dist]+=1
        #     outgoing[src]+=1
        # for i in range(1,n+1):
        #     if incoming[i] == (n-1) and outgoing[i] == 0:
        #         return i
        # return -1 

        # Delta method with reduced space Delta = incoming - outgoing = n-1 -0 => n-1
        if n ==1:
            return 1
        from collections import defaultdict
        delta = defaultdict(int)
        for src,dist in trust:
            delta[src]-=1
            delta[dist]+=1
        for i in range(1,n+1):
            if delta[i] == (n-1):
                return i
        return -1 

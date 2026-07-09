class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # We are using undirected graph. So both edges, adjaceny list, visit hashset are used.

        from collections import defaultdict
        adj = defaultdict(list)
        # we loop through the equations and build the adj list
        for i, eq in enumerate(equations):
            # We enumerate to get index and value so that when we add weights we can target the corresponding values.
            a,b = eq
            adj[a].append([b,values[i]])
            adj[b].append([a,1/values[i]]) #Integer division in python which is what we exactly need.
        
        def bfs(src, target):
            if src not in adj or target not in adj: # If we don't find either of the nodes in adj list, we simply return negative one, as it is clearly stated in the problem that " If a single answer cannot be determined, return -1.0"
                return -1
            from collections import deque
            q, visit = deque(), set()
            q.append([src,1])
            # We create the queue and initialise the weight as 1
            visit.add(src)
            # We add the src node to our visit hashset
            while q:
                node,w = q.popleft()
                # We pop 2 values, both the node and the current weight
                if node == target:
                    return w
                # If the current node has already reached target, we simply want to return the current weight
                for neigh,weight in adj[node]:
                    # We go through the neighbours. We traverse both the neigh node and the weight to travel.
                    if neigh not in visit:
                        # We check if the node is not already been visited.
                        q.append([neigh,w * weight])
                        # We add the visited node to the queue as well as we multiply the current weight and the new weight to travel to the next node.
                        visit.add(neigh)
                        # We add the neigh to the visit set
            # When queue becomes empty we return -1
            return -1
        # We run bfs using list comprehension and hence we return that list of answers from the queries input.
        return [bfs(q[0],q[1]) for q in queries]
            

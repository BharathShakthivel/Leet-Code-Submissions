# Union Find Method
class Union:
    def __init__(self,n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    def find(self,x):
        while x!= self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    def union(self,n1,n2):
        p1,p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True
            
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = Union(len(accounts))
        emailtoAcc = {}
        for i,a in enumerate(accounts):
            for e in a[1:]:
                if e in emailtoAcc:
                    uf.union(i,emailtoAcc[e])
                else:
                    emailtoAcc[e] = i
        from collections import defaultdict
        
        acc_merge = defaultdict(list)
        for e, i in emailtoAcc.items():
            leader = uf.find(i)
            acc_merge[leader].append(e)
        
        res = []
        for i,e in acc_merge.items():
            name = accounts[i][0]
            res.append([name]+sorted(acc_merge[i]))
        return res

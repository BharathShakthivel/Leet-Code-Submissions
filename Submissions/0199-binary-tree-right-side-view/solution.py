# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Breadth First Search - BFS
        res = []
        q = collections.deque([root])
        while q:
            right_most_node = None # Initially we set it to Null
            q_len = len(q)
            for i in range(q_len):
                node = q.popleft()
                if node:
                    right_most_node = node # Once we loop through current length of the queue, we are guarenteed that the last node owuld be the right most node. So we will append that val to our result.
                    q.append(node.left)
                    q.append(node.right)
            if right_most_node: # The right most node would be the last node of the current instance of the Queue.
                res.append(right_most_node.val)
        return res
        

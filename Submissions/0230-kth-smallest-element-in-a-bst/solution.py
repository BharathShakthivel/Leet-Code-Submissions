# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # DFS - Inorder Traversal
        # stack = []
        # if not root:
        #     return -1
        # def dfs(node,stack):
        #     if not node:
        #         return
        #     dfs(node.left,stack)
        #     stack.append(node.val)
        #     dfs(node.right,stack)
        # dfs(root,stack)
        # if stack:
        #     return stack[k-1]
        # return -1

        #  Iterative Solution
        n = 0
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur=cur.left
            cur = stack.pop()
            n+=1
            if n == k:
                return cur.val
            cur=cur.right


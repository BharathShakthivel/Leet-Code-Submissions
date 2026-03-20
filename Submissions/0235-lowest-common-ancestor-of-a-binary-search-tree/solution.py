# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

        # In a BST, the LCA is the first node where p and q split into different directions
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root  # start from the root of the BST
        
        while cur:
            # If both p and q are greater than current node,
            # LCA must be in the right subtree
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            
            # If both p and q are smaller than current node,
            # LCA must be in the left subtree
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            
            # Otherwise, we have found the split point:
            # one node is on one side and the other is on the other side
            # OR one of them is equal to current node
            # Hence, current node is the LCA
            else:
                return cur
            

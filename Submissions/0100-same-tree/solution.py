# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Mental logic:
# 1) If both nodes are None, the trees match at this position, so return True.
# 2) If only one node is None, or their values differ, the trees are not the same, so return False.
# 3) Otherwise, the current nodes match, so recursively check:
#    - left subtree with left subtree
#    - right subtree with right subtree
# 4) Both recursive checks must be True for the trees to be identical.

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val!=q.val:
            return False
        return (self.isSameTree(p.left,q.left)) and (self.isSameTree(p.right,q.right))
            

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Traverse every node in root and check whether the subtree
# starting at that node is identical to subRoot




class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return False
            if sameTree(node,subRoot):
                return True
            
            # If we reach an empty node, subRoot cannot start here
            # If the trees match at the current node, return True
            # Otherwise keep searching in the left or right subtree
            return dfs(node.left) or dfs(node.right)

            
        # Check whether two trees are exactly identical
        # If both nodes are empty, they match
        # If only one is empty or values differ, they do not match
        # Otherwise both left and right children must also match
        def sameTree(node_1,node_2):
            if not node_1 and not node_2:
                return True
            if not node_1 or not node_2 or node_1.val != node_2.val:
                return False
            return (sameTree(node_1.left,node_2.left)) and (sameTree(node_1.right,node_2.right))
        return dfs(root)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        # Iterative
        # if not root:
        #     return TreeNode(val)
        # cur = root
        # while True:
        #     if val > cur.val:
        #         if cur.right:
        #             cur=cur.right
        #         else:
        #             cur.right = TreeNode(val)
        #             return root
        #     else:
        #         if cur.left:
        #             cur=cur.left
        #         else:
        #             cur.left = TreeNode(val)
        #             return root
        # return root

        # Recursive
        if not root:
            return TreeNode(val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right,val)
        else:
            root.left = self.insertIntoBST(root.left,val)
        return root

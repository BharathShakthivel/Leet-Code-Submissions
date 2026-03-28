# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
        Mental model: “Root splits the world”

        Think of the two arrays as giving you two different clues:

        Preorder = Root comes first
        First value is always the root of the current subtree
        Inorder = Left | Root | Right
        Root divides the left subtree from the right subtree

        So every recursive step is just:

        Take first from preorder → find it in inorder → split left and right → repeat

        Super short memory phrase
        “Preorder picks, inorder splits.”

        This is the easiest phrase to remember.

        preorder tells you what node to create
        inorder tells you where left/right parts are
    '''
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root

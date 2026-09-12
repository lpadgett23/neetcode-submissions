# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        i = 0

        def inorder(node):
            if node:
                inorder(node.left)
                stack.append(node.val)
                
                inorder(node.right)
            
        inorder(root)

        # while stack:
        #     v = stack.pop(i)
        #     res.append(v)

        return stack
# Remember that for a BST to be valid, it is not just the immediate children that have to fit the definition

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        prev = None

        check = True

        def inorder(root):
            nonlocal check, prev

            if root == None:
                return

            inorder(root.left)

            if prev != None and root.val <= prev:
                check = False
                return

            prev = root.val

            inorder(root.right)

        inorder(root)

        return check
        
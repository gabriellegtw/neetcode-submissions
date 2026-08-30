# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        stack = []
        tree1 = []
        tree2 = []

        stack.append(p)

        while stack:
            root = stack.pop()
            if root == None:
                tree1.append(0)
                continue
            else:
                tree1.append(root.val)

            stack.append(root.left)
            stack.append(root.right)

        stack.append(q)

        while stack:
            root = stack.pop()
            if root == None:
                tree2.append(0)
                continue
            else:
                tree2.append(root.val)

            stack.append(root.left)
            stack.append(root.right)

        return tree1 == tree2

            

        
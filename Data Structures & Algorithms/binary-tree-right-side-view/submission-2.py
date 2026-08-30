# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []

        if root is None:
            return self.result

        def helper(node, depth):
            if node is None:
                return

            if len(self.result) == depth:
                self.result.append(node.val)

            helper(node.right, depth + 1)
            helper(node.left, depth + 1)
            
        helper(root, 0)

        return self.result
        
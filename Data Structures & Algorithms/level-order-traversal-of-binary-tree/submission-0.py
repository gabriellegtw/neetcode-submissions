# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.result = []

        def helper(node, depth):
            if node is None:
                return 

            if len(self.result) < depth + 1:
                self.result.append([])

            self.result[depth].append(node.val)
            
            # Append the elements to the current level
            helper(node.left, depth + 1)
            helper(node.right, depth + 1)

        helper(root, 0)

        return self.result
        
# Takeaway: Remember that in recursion, the values within the recurive
# function does not affect the value outside the function - they are different scopes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def helper(root, curr) -> int:
            if root == None:
                return curr

            curr += 1

            return max(helper(root.right, curr), helper(root.left, curr))

        return helper(root, 0)
            
        
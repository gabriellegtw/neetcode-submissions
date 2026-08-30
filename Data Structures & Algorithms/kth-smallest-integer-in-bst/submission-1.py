# For recursive solution, remember that the structure is base case, recurse left,
# logic to handle centre, recurse right

# Remember that recursive function goes all the way to the base case 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        stack = []
        curr = root
        count = k
        
        def dfs(root) -> int:
            nonlocal stack, curr, count
            while stack or curr:
                while curr:
                    stack.append(curr)
                    curr = curr.left
                curr = stack.pop()
                count = count - 1
                if count == 0:
                    return curr.val
                curr = curr.right

        return dfs(root)

        
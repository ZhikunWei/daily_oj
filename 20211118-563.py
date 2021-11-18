# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root) -> int:
        if not root:
            return 0
        self.res = 0
        self.tree_sum(root)
        return self.res

    def tree_sum(self, root):
        if not root:
            return 0
        left_sum = self.tree_sum(root.left)
        right_sum = self.tree_sum(root.right)
        self.res += abs(left_sum - right_sum)
        return left_sum + right_sum + root.val

t = Solution().findTilt()
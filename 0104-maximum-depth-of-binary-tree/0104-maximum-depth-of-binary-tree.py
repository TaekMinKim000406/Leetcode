# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depths = [] 
        def dps(current, depth):
            if current is None:
                depths.append(depth)
            elif current.left is None and current.right is None:
                depths.append(depth+1)
            else:
                if current.left:
                    dps(current.left, depth+1)
                if current.right:
                    dps(current.right, depth+1)

        dps(root,0)
        return max(depths)            
            

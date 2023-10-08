# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return
        sums = []
        def rcsv(cur_node, cur_sum):
            if cur_node.left is None and cur_node.right is None:
                sums.append(cur_sum+cur_node.val)
            if cur_node.left:
                rcsv(cur_node.left, cur_sum+cur_node.val)
            if cur_node.right:
                rcsv(cur_node.right, cur_sum+cur_node.val)    

        rcsv(root, 0)
        
        if targetSum in sums:
            return True


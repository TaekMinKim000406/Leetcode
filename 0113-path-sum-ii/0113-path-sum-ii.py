# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        if root == None:
            return root
        paths = []
        def findpath(cur_node, cost, path):
            if cur_node.left == None and cur_node.right == None and cost == targetSum:
                paths.append(path)
            else:
                if cur_node.left != None:
                    findpath(cur_node.left, cost+cur_node.left.val, path+[cur_node.left.val])
                if cur_node.right != None:
                    findpath(cur_node.right, cost+cur_node.right.val, path+[cur_node.right.val])

        findpath(root,root.val,[root.val])
        return paths

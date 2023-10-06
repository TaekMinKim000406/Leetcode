# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        nodes = [root]
        values = []
        while len(nodes)>0:
            next_nodes = []
            value = []
            while len(nodes)>0:
                node = nodes.pop(0)
                if node != None:
                    value.append(node.val)
                    next_nodes.append(node.left)
                    next_nodes.append(node.right)
            if len(value)>0:        
                values.append(value)
                nodes = next_nodes
        return values
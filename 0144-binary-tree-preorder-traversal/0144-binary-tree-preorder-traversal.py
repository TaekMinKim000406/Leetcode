# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return
        nodes = [root]
        values = []
        while nodes:
            node = nodes.pop()
            values.append(node.val)
            
            if node.right:
                nodes.append(node.right)
            if node.left:
                nodes.append(node.left)
            

        return values

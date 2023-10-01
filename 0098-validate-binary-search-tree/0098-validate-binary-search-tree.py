# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #중위 순회하고 value를 순서대로 담았을 떄 오름차순이면 됨
        Nodes = []
        def inorder(node):
            if node.left != None:
                inorder(node.left)
            Nodes.append(node.val)
            if node.right != None:
                inorder(node.right)


        inorder(root)

        for i in range(0, len(Nodes)-1):
            if Nodes[i]>=Nodes[i+1]:
                return False
        return True        


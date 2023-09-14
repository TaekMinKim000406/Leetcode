# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # if root == None:
        #     return root

        # stack  = []
        # result = []

        # stack.append(root)
        # result.append([root.val])
        
        # right_to_left = True
        # while stack:
        #     cur = stack[0]
        #     stack = stack[1:]
        #     if cur != None and not right_to_left:
        #         if cur.left != None:
        #             stack.append(cur.left)
        #         if cur.right != None:    
        #             stack.append(cur.right)
        #         if cur.right is not None and cur.left is not None:
        #             result.append([cur.left.val, cur.right.val])
        #         elif cur.right is not None and cur.left is None:
        #             result.append([cur.right.val])
        #         elif cur.right is None and cur.left is not None:
        #             result.append([cur.left.val])
        #         right_to_left = True
        #     elif cur != None and right_to_left:
        #         if cur.right != None:    
        #             stack.append(cur.right)
        #         if cur.left != None:
        #             stack.append(cur.left)
        #         if cur.right is not None and cur.left is not None:
        #             result.append([cur.right.val, cur.left.val])
        #         elif cur.right is not None and cur.left is None:
        #             result.append([cur.right.val])
        #         elif cur.right is None and cur.left is not None:
        #             result.append([cur.left.val])    
        #         right_to_left = False
        
        # return result


        if not root:
            return []

        stack = [root]
        result = []

        right_to_left = False
        while stack:
            level = []
            next_stack = []
            for node in stack:
                level.append(node.val)
                if node.left:
                    next_stack.append(node.left)
                if node.right:
                    next_stack.append(node.right)
            if right_to_left:
                level = level[::-1]  # 현재 레벨의 값을 역순으로 변경
            result.append(level)
            right_to_left = not right_to_left
            stack = next_stack

        return result

        

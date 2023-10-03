# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def rob_helper(node):
            if not node:
                return (0, 0)  # (포함할 때의 최대 가치, 포함하지 않을 때의 최대 가치)

            # 왼쪽 서브트리와 오른쪽 서브트리에서 최대 가치 계산
            left_with, left_without = rob_helper(node.left)
            right_with, right_without = rob_helper(node.right)

            # 현재 노드를 포함할 때의 최대 가치와 포함하지 않을 때의 최대 가치 계산
            with_current = node.val + left_without + right_without
            without_current = max(left_with, left_without) + max(right_with, right_without)

            return (with_current, without_current)

        # 최종 결과 반환
        with_root, without_root = rob_helper(root)
        return max(with_root, without_root)

        # #시간 초과
        # def rc(current, cur_yes):
        #     if current == None:
        #         return 0
        #     cost = 0     
        #     if cur_yes: 
        #         cost += current.val
        #     if cur_yes:
        #         return cost + rc(current.left, False) + rc(current.right, False)
        #     else:        
        #         return cost + max(rc(current.left, True), rc(current.left, False)) + max(rc(current.right, True), rc(current.right, False))    


        # return max(rc(root, True) ,rc(root, False))


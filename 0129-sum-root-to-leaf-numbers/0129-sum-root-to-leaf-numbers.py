# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nums = []
        def dps(cur, num):
            if cur.left == None and cur.right == None: #leaf node
                nums.append(num*10+cur.val)
            else:
                num = num*10+cur.val
                if cur.left:
                    dps(cur.left, num)
                if cur.right:
                    dps(cur.right, num)        

        dps(root, 0)
        print(nums)
        return sum(nums)

        # nums = []
        # values = []
        # nodes = [root]
        # while nodes:
        #     node = nodes.pop(0)
        #     if node is None:
        #         values.append(None)
        #     else:
        #         values.append(node.val)
        #         nodes.append(node.left)
        #         nodes.append(node.right)
        # print(values)            
        # dp = [values[0]]
        # for i in range(1,len(values)):
        #     if values[i]!=None:
        #         dp.append(dp[(i-1)//2]*10 + values[i])
        #     else:
        #         dp.append(None)    
        # print(dp)
        # num = 0     
        # for i in range(len(dp)//2):
        #     if dp[2*i+1] ==None and  dp[2*i+2] == None:
        #         if dp[i]!= None:
        #             num += dp[i]
        # return num    

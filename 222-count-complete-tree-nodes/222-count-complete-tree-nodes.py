# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
    
        def fun(root):
            if root==None:
                return 0
            lh=0
            rh=0
            temp=root
            while(temp.left!=None):
                lh+=1
                temp=temp.left
            temp=root
            while(temp.right!=None):
                rh+=1
                temp=temp.right
            if (lh==rh):
                return ((2**(lh+1))-1)
            else:
                return 1+fun(root.left)+fun(root.right)
        return fun(root)
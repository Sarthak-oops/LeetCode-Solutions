# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        a=[]
        def traversal(root):
            if root==None:
                return
            traversal(root.left)
            a.append(root.val)
            
            traversal(root.right)
        traversal(root1)
        traversal(root2)
        print(a)
        a.sort()
        return a
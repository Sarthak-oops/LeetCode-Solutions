# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        a=[]
        b=[]
        def traversal(root,l):
            if root==None:
                return
            traversal(root.left,l)
            l.append(root.val)
            
            traversal(root.right,l)
        traversal(root1,a)
        traversal(root2,b)
        s1,s2=0,0
        print(a)
        print(b)
        li=[]
        e1=len(a)-1
        e2=len(b)-1
        while(s1<=e1 and s2<=e2):
            if a[s1]<=b[s2]:
                li.append(a[s1])
                s1+=1
            else:
                li.append(b[s2])
                s2+=1
        li.extend(a[s1:])
        li.extend(b[s2:])
        return li
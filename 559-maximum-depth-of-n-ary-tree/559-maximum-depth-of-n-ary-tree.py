"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        depth=0
        q=[]
        tq=[root]
        if root==None:
            return 0
        while tq:
            q=tq
            tq=[]
            depth+=1
            while(q):
                x=q.pop(0)
                for i in x.children:
                    tq.append(i)
        return depth
                
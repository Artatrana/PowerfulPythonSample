# Given two non-empty binary tree s and t, check whether tree t has exactly 
# same strucure and node values with a subtree of s. A subtree s is a tree consist
# of note is s and all of this nodes's descendeants. The tree s could also be
# considered as a subtree of itself.

class TreeNode:
    def __init__(self, x):
        self.val = x 
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None and t is None:
            return True 
        if t is None:
            return True
        if s is None:
            return False
        return self.isSame(s,t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


    
    def isSame(self, s, t):
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        return s.val == t.val and self.isSame(s.left ,t.left) and self.isSame(s.right ,t.right)
    

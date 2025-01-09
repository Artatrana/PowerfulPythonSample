# Symmetric Tree 
# Given a tree check whether it is a mirror or itself 
# Definition of a tree
class TreeNode:
    def __init__(self,x) -> None:
        slef.val = x
        self.left = None
        self.right = None

class Solution:
    def symmetic(self, root: TreeNode) -> bool:
        if root is None:
            return True 
        
        return 
    
        def ismirror(self, leftroot, rightroot):
            if leftroot.val and rightroot: # not None
                return leftroot.val == rightroot.val and self.ismirror(leftroot.left, righroot.right) and  self.ismirror(leftroot.right, righroot.left)
            
            return leftroot == rightroot
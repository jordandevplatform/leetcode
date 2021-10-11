def diameter(self,root):
        if not root:
            return 0
        ld = self.diameter(root.left)
        rd = self.diameter(root.right)
        self.d = max(self.d, ld+rd)
        return max(ld,rd) + 1
        
def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.d = 0
        self.diameter(root)
        return self.d
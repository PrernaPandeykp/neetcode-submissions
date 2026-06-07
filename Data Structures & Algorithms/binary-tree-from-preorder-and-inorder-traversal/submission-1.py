# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderMap = {}
        for i in range(len(inorder)):
            inorderMap[inorder[i]] = i

        preorderIdx = 0
    
        def dfs(l, r): 
            nonlocal preorderIdx, inorderMap    
            if l>r:
                return
            
            root = preorder[preorderIdx]
            preorderIdx +=1
            
            newTree = TreeNode(root)

            idx = inorderMap[root]

            newTree.left = dfs(l, idx-1)
            newTree.right = dfs(idx+1, r)

            return newTree

        return dfs(0, len(inorder)-1)

        
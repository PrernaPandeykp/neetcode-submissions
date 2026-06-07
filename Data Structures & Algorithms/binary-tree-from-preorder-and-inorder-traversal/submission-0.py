# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder and not preorder:
            return
        root = preorder[0]
        newTree = TreeNode(root)

        idx = inorder.index(root)

        newTree.left = self.buildTree(preorder[1:idx + 1], inorder[:idx])
        newTree.right = self.buildTree(preorder[idx + 1:], inorder[idx+1:])

        return newTree

        
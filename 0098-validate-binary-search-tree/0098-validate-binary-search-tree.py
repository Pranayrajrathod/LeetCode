# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # def isvalid(root):
        #     if(root==None):
        #         return True
        #     if(root.left==None and root.right==None):
        #         return True
        #     lv=isvalid(root.left)
        #     rv=isvalid(root.right)
        #     cv=root.val
        #     if(root.left!=None):
        #         lval=root.left.val
        #         if(cv>lval and lv):
        #             return True
        #         else:
        #             return False
        #     if(root.right!=None):
        #         rval=root.right.val
        #         if(cv<rval and rv):
        #             return True
        #         else:
        #             return False
        #     lval=root.left.val
        #     rval=root.right.val
            
        #     if(cv<rval and cv>lval):
        #         return lv and rv 
        #     return False
        # return isvalid(root)

        def inorder(root,arr):
            if(root==None):
                return arr
            inorder(root.left,arr)
            arr.append(root.val)
            inorder(root.right,arr)
            return arr
        arr=inorder(root,[])
        l=len(arr)
        if(l==0):
            return True
        prev=arr[0]
        for i in range (1,l):
            if(prev<arr[i]):
                prev=arr[i]
            else:
                return False
        return True
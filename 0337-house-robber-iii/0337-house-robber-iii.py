# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def robing(root):
            if(root==None):
                return [0,0]

            l=robing(root.left)
            r=robing(root.right)
            print(l,r)
            #[rob current, don't rob current houses]
            return [l[1]+r[1]+root.val,max(l[1],l[0])+max(r[1],r[0])]

        ans=robing(root)
        
        return max(ans[0],ans[1]) 
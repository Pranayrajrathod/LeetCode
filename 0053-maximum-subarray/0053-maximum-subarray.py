class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        cs=0
        mx=nums[0]
        for each in nums:
            cs+=each
            mx=max(mx,cs)
            if(cs<0):
                cs=0
            else:
                mx=max(mx,cs)
        return mx
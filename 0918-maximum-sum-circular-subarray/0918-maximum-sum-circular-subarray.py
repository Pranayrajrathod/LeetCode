class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        l=len(nums)
        mx=float('inf')
        cs=0
        ts=sum(nums)
        for i in range (1,l):
            cs+=nums[i]
            mx=min(cs,mx)
            if(cs>=0):
                cs=0
        mx=ts-mx
        cs=0
        for i in range(l):
            cs+=nums[i]
            mx=max(mx,cs)
            if(cs<0):
                cs=0
        return mx
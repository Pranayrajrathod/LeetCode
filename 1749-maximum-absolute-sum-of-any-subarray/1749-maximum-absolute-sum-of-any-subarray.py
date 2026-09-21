class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:

        l=len(nums)
        mx=-float('inf')
        sm=0
        ps=0
        ns=0
        for i in range(l):
            if(ps<0):
                ps=0
            ps+=nums[i]
            mx=max(ps,mx)
        ps=0
        for i in range (l):
            if ps>0:
                ps=0
            ps+=nums[i]
            mx=max(mx,abs(ps))
        return mx

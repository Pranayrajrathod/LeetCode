class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        sp=0
        l=len(nums)
        mp=0
        pp=1
        sp=1
        if(l==1):
            return nums[0]
        for i in range (l):
            sp*=nums[i]
            pp*=nums[-(i+1)]
            mp=max(mp,sp,pp)
            if(sp==0):
                sp=1
            if(pp==0):
                pp=1
        return mp

class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        d={0:-1}

        l=len(nums)
        if(l==1):
            return False

        ps=0
        for i in range (l):
            ps=ps+nums[i]
            rem=ps%k
            if(rem in d):
                if(i-d[rem]>=2):
                    return True
            else:
                d[rem]=i
        # if(d[0]>-1):
        #     return True
        return False

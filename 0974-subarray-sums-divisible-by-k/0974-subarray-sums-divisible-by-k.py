from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        l=len(nums)
        ps=0
        c=0
        d=defaultdict(int)
        d[0]=1
        for i in range (l):
            ps+=nums[i]
            rem=(ps)%k 
            c+=d[rem]   
            d[rem]+=1
        return c
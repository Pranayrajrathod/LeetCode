class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        l=len(nums)
        ans=0
        for i in range (l):
            c=0
            for j in range (i,l):
                if(nums[j]==target):
                    c+=1
                if((2*c)>(j-i+1) or (j==i and c==1)):
                    ans+=1
        return ans
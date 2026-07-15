from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def same(a,b):
            al=len(a)
            bl=len(b)
            for each in a:
                if(a[each]!=b[each]):
                    return False
            return al==bl
        pl=len(p)
        sl=len(s)
        ac=Counter(p)
        ans=[]
        for i in range (0,sl-pl+1):
            bc=Counter(s[i:i+pl])
            if(same(ac,bc)):
                ans.append(i)
        return ans
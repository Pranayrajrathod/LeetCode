class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=""
        for each in s:
            if(each.isalnum()):
                t+=each.lower()
        l=len(t)
        i=0
        j=l-1
        while(i<j):
            if(t[i]==t[j]):
                i+=1
                j-=1
            else:
                return False
        return True
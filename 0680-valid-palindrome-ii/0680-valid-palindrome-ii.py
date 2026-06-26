class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispal(s,l):
            i=0
            j=l-1
            while(i<=j):
                if(s[i]!=s[j]):
                    return False
                else:
                    i+=1
                    j-=1
            return True 
        i=0
        l=len(s)
        j=l-1

        while(i<=j):
            if(s[i]==s[j]):
                i+=1
                j-=1
            else:
                temp1=s[:i]+s[i+1:]
                temp2=s[:i-1]+s[i:]
                temp4=s[:j-1]+s[j:]
                temp3=s[:j]+s[j+1:]
                
                print(i,j,temp1,temp2)

                if(ispal(temp1,l-1) or ispal(temp2,l-1) or ispal(temp3,l-1) or ispal(temp4,l-1)):
                    return True
                else:
                    return False
        return True
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        res = str(x)
        l=0
        r=len(res)-1

        while l<r:
            if res[l]==res[r]:
                l+=1
                r-=1
                continue
            if res[l]!=res[r]:
                return False
            
        return True
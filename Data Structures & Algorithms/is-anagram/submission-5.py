class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count={}
        count2={}

        if len(s)!=len(t):
            return False

        for i in range(len(s)):
            count[s[i]]=count.get(s[i],0)+1
            count2[t[i]]=count2.get(t[i],0)+1

        return count==count2
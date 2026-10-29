class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        
        index=set()

        map1={}

        for i, n in enumerate(keyboard):
            map1[n]=i

        prev=0
        res=0
        for j in word:
            res+=abs(map1[j]-prev)
            prev=map1[j]
        return res
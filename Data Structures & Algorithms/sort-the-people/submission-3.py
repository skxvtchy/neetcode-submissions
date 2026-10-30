class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        

        count ={}
        res =[]

        for h, n in zip(heights, names):
            count[h]=n

        for h in reversed(sorted(heights)):
            res.append(count[h])
        
        return res
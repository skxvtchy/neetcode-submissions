class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []

        for i in nums:
            count[i]=count.get(i,0)+1

        for i in range(k):
            maxi = max(count, key=count.get)
            res.append(maxi)

            del count[maxi]
       
        return res
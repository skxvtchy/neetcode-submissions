class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []

        for i in nums:
            count[i]=count.get(i,0)+1

        for i in range(k):
            max_key = max(count, key=count.get)
            res.append(max_key)
            # Remove it from the map
            del count[max_key]
        # print(max(count.values()))
        # print(max(count))
        # print(min(count.values()))
        # print(min(count))
        return res
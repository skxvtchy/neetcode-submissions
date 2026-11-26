class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        
        heapq.heapify(prices)
        temp = money

        for i in range(2):
            money -= heapq.heappop(prices)
        
        return money if money >= 0 else temp
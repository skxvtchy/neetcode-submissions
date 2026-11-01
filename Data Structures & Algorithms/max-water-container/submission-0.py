class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        i=heights
        maxi = 0
        while l!=r:
            
            if i[l]<=i[r]:
                maxi=max(maxi,i[l]*(r-l))
                l+=1
            elif i[r]<i[l]:
                maxi=max(maxi,i[r]*(r-l))
                r-=1
        return maxi
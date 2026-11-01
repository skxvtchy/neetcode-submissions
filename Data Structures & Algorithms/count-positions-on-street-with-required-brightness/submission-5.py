class Solution:
    def meetRequirement(self, n: int, lights: List[List[int]], requirement: List[int]) -> int:
        count = [0]*n


        for i,j in lights:
            l=i-j
            r=i+j

            if l<0:
                l=0
            if r>=len(requirement):
                r=len(requirement)-1


            
            for x in range(l,r+1):
                # print([l:r])
                # pass
                count[x]+=1
            

        res = 0
        for i in range(len(count)):
            if requirement[i]<=count[i]:
                res+=1

        return res

                       


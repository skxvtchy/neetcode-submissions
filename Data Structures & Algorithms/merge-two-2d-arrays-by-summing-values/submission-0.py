class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        
        count={}

        for i, value in nums1:
            count[i]=value
        for i, value in nums2:
            if i in count:
                count[i]+=value
            else:
                count[i]=value

        arr =[]

        for i in sorted(count):
            arr.append([i,count[i]])

        return arr
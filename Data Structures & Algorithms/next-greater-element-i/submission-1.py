class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        for i in range(len(nums1)):
            idx=0
            for x in range(len(nums2)):
                if nums1[i]==nums2[x]:
                    idx=x
                    break
            found = False
            for j in range(idx + 1, len(nums2)):
                if nums2[j] > nums1[i]:
                    res.append(nums2[j])
                    found = True
                    break
            if not found:
                res.append(-1)
        return res
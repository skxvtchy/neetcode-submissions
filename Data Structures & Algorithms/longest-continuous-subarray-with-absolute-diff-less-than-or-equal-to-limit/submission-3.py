class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        count = 0
        mini= 0
        maxi = 0
        for i in range(len(nums)):
            mini = nums[i]
            maxi = nums[i]
            for j in range(i+1,len(nums)):
                mini = min(mini, nums[j])
                maxi = max(maxi, nums[j])
                if maxi-mini>limit:
                    break   
            
                count = max(count, j-i+1)

            count = max(count, 1)

        return count
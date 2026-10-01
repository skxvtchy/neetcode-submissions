class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # sort = sorted(nums)
        count={}

        for i, n in enumerate(nums):
            count[n] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in count and i != count[diff]:
                return [i,count[diff]]
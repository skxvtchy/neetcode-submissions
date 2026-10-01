class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # sort = sorted(nums)
        count={}

        for i in range(len(nums)):
            count[nums[i]]=i


        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in count and i != count[diff]:
                return [i,count[diff]]
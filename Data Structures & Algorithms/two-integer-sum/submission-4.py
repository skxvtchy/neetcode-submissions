class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = 1
        
        res = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in res:
                return [res[complement], i]
            res[nums[i]]=i


        return False
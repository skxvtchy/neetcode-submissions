class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        l=0
        check = 0
 

        for i in range(1,len(nums)):

 
            if check ==1:
                if nums[i]>nums[l]:
                
                    return False
            if check ==2:
                if nums[i]<nums[l]:
        
           
                    return False
            if nums[i]<nums[l]:
                check = 1
  
                
            if nums[i]>nums[l]:
                check = 2
            l+=1
        
        return True
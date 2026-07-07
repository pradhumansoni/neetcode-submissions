class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted = nums.sort()
        idx = 0
        while idx <= len(nums)-2:
            if nums[idx] == nums[idx+1]:
                return True
                break
            else:
                idx+=1  
        return False 
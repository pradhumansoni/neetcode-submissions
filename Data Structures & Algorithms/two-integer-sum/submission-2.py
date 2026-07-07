class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Target Time -> O(n) 
        hash ={}
        for i,val in enumerate(nums):
            remain = target - val
            if remain in hash:
                return [hash[remain] , i]
            hash[val] = i
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Sub Optimal Approach
        # TC -> O(n) , SC -> O(n)
        # Find the prefix and suffix arrays
        # Then the mapped product is the final answer
        n = len(nums)
        final = [1]*n 
        prefix = 1
        suffix = 1
        for i in range(1, n):
            final[i] = final[i-1] * nums[i-1]
        for i in range(n-2 , -1,-1):
            suffix*= nums[i+1]
            final[i]*=  suffix
        return final


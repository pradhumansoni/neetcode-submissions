class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Sub Optimal Approach
        # TC -> O(n) , SC -> O(n)
        # Find the prefix and suffix arrays
        # Then the mapped product is the final answer
        n = len(nums)
        final = []
        prefix = [1]*n
        suffix = [1]*n
        for i in range(1, n):
            prefix[i] = prefix[i-1]*nums[i-1]
        for i in range(n-2 , -1,-1):
            suffix[i] = suffix[i+1] * nums[i+1]
        return [i*j for i,j in zip(prefix , suffix)]


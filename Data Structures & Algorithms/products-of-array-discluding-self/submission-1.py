class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Logic:
        1. divide the array into two parts left and right of index i
        2. find each product and multiply it into final.
        '''
        final = []
        n = len(nums)
        for i in range(n):
            prod = 1
            for j in range(n):
                if i!=j:
                    prod *= nums[j]
            final.append(prod)
        return final
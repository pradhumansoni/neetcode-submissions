from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = Counter(nums)
        values = set(sorted(hash.values())[-k:])
        final=[]
        for key,value in hash.items():
            if value in values:
                final.append(key)
        return final
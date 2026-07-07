from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        arr=[]
        for key,value in count.items():
            arr.append([value,key])
        arr.sort()
        final = []
        # return arr
        for _ in range(k):
            final.append(arr.pop()[1])
        return final

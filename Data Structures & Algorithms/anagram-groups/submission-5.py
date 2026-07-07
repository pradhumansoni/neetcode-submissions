from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        for word in strs:
            count = [0]*26
            for char in word:
                idx = ord(char) - ord('a')
                count[idx] +=1
            key = tuple(count)
            hash[key].append(word)
        return list(hash.values())
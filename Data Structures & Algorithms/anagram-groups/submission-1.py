class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Method 1: Hashing Based on Sorted String
        hash= {}
        for word in strs:
            key = ''.join(sorted(word)) 
            if key not in hash:
                hash[key] = [word] 
            else:
                hash[key] = hash[key] + [word]
        return list(hash.values())
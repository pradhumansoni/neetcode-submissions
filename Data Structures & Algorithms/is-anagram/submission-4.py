from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table1 = Counter(s)
        table2 = Counter(t)
        return table1 == table2

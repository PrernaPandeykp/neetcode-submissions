class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first, sec= {}, {}
        for i in s:
            first[i] = first.get(i,0) + 1

        for i in t:
            sec[i] = sec.get(i,0) +1

        return first == sec
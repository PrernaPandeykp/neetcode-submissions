class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = {}
        l= 0
        res = 0
        for r in range(len(s)):
            if s[r] in charMap:
                l = max(l, charMap[s[r]] + 1)

            charMap[s[r]] = r
            res = max(r-l +1, res)

        return res

        
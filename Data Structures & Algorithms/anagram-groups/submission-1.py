class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashStr = {}
        for st in strs:
            k = "".join(sorted(st))
            if k not in hashStr:
                hashStr[k] = []

            hashStr[k].append(st)
        return list(hashStr.values())


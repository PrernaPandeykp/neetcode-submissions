class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashStr = defaultdict(list)
        
        for st in strs:
            k = "".join(sorted(st))
            hashStr[k].append(st)
        
        return list(hashStr.values())


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sMap = {}
        tMap = {}

        for charS, charT in zip(s, t):
            sMap[charS] = sMap.get(charS, 0) + 1
            tMap[charT] = tMap.get(charT, 0) + 1
        
        return sMap == tMap
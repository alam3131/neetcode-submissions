class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        seen = set()
        maxLength = 0

        while r < len(s):
            if s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1

            maxLength = max(maxLength, r - l + 1)
            seen.add(s[r])
            r += 1
        
        return maxLength

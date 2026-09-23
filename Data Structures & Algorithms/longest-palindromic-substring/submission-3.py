class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.maxLength = 0
        self.longestSubstringIndex = (0, 0)
        
        def expand(l, r):
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    strLength = r + 1 - l
                    if strLength > self.maxLength:
                        self.maxLength = strLength
                        self.longestSubstringIndex = (l, r)
                else:
                    break
                l -= 1
                r += 1
        
        for i in range(len(s)):
            # Substring is odd
            expand(i, i)

            # Substring is even
            expand(i, i+1)

        l, r = self.longestSubstringIndex
        return s[l : (r + 1)]
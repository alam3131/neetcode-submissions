class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.maxLength = 0
        self.longestSubstring = ""
        
        def expand(l, r):
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    strLength = r + 1 - l
                    if strLength > self.maxLength:
                        self.maxLength = strLength
                        self.longestSubstring = s[l : (r + 1)]
                else:
                    break
                l -= 1
                r += 1
        
        for i in range(len(s)):
            # Substring is odd
            expand(i, i)

            # Substring is even
            expand(i, i+1)

        return self.longestSubstring
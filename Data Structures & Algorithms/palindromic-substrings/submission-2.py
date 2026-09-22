class Solution:
    # Checking and expanding around centers: 2n - 1 centers
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def countSubstrings(self, s: str) -> int:
        self.count = 0
        
        def expand(l, r):
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    self.count += 1
                else:
                    break
                l -= 1
                r += 1
        
        for i in range(len(s)):
            # Substring is odd
            expand(i, i)

            # Substring is even
            expand(i, i+1)

        return self.count
#include <unordered_map> 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {}

        for i in range(len(strs)):
            # Initialize char array
            charCount = [0] * 26
            # Create char count array for str
            for j in strs[i]:
                charCount[ord(j) - 97] += 1
            # Add char count tuple to map
            if tuple(charCount) in anagramMap:
                anagramMap[tuple(charCount)].append(strs[i])
            else:
                anagramMap[tuple(charCount)] = [strs[i]]

        # Collect all map values into a single array
        resultArr = []
        for key, val in anagramMap.items():
            resultArr.append(val)
        
        return resultArr
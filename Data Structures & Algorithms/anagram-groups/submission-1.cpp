#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> hashMap;
        vector<vector<string>> result;

        for (int i = 0; i < strs.size(); i++) {
            vector<int> charCount(26, 0); // Used as the key
            
            // Get the char count for the string
            for (char c : strs[i]) {
                charCount[(int)c - 97]++;
            }

            string key;
            for (int count : charCount) {
                key += "#" + to_string(count);  // Delimiter prevents collisions
            }

            auto iter = hashMap.find(key);
            if (iter != hashMap.end()) {
                hashMap[key].push_back(strs[i]);
            } else {
                hashMap[key] = {strs[i]};
            }
        }

        for (const auto& [key, value] : hashMap) {
            result.push_back(value);
        }

        return result;
    }
};

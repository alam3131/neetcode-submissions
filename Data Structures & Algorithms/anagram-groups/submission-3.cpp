#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> hashMap;
        vector<vector<string>> result;

        for (const auto& s : strs) {
            vector<int> charCount(26, 0);
            for (char c : s) {
                charCount[c - 'a']++;
            }

            string key;
            for (int count : charCount) {
                key += "#" + to_string(count);
            }

            hashMap[key].push_back(s);
        }

        for (const auto& [key, value] : hashMap) {
            result.push_back(value);
        }

        return result;
    }
};

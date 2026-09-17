#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> hashMap;
        vector<vector<string>> result;

        for (int i = 0; i < strs.size(); i++) {
            string str = strs[i];
            sort(str.begin(), str.end());

            auto iter = hashMap.find(str);
            if (iter != hashMap.end()) {
                hashMap[str].push_back(strs[i]);
            } else {
                hashMap[str] = {strs[i]};
            }
        }

        for (const auto& [key, value] : hashMap) {
            result.push_back(value);
        }

        return result;
    }
};

#include <unordered_map>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }

        unordered_map<char, int> hash_s;
        unordered_map<char, int> hash_t;

        for (int i = 0; i < s.size(); i++) {
            auto char_s = hash_s.find(s[i]);

            if (char_s != hash_s.end()) {
                hash_s[s[i]]++;
            } else {
                hash_s[s[i]] = 1;
            }
        }

        for (int i = 0; i < t.size(); i++) {
            auto char_t = hash_t.find(t[i]);

            if (char_t != hash_t.end()) {
                hash_t[t[i]]++;
            } else {
                hash_t[t[i]] = 1;
            }
        }

        if (hash_s == hash_t) {
            return true;
        }

        return false;
    }
};

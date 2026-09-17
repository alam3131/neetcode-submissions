#include <cctype>
#include <iostream>

class Solution {
public:
    bool isPalindrome(string s) {
        // Formats the string to be alphanumeric and lowercase
        for (int k = 0; k < s.size();) {
            if (!isalnum(s[k])) {
                s.erase(k, 1);
            }  else {
                k++;
            }
        }

        int i = 0, j = s.size() - 1;
        // Performs the two pointer check
        while (i < j) {
            cout << "s[i]:" << s[i] << "  ";
            cout << "s[j]:" << s[j] << endl;
            if (tolower(s[i]) != tolower(s[j])) {
                return false;
            }
            i++;
            j--;
        }

        return true;
    }
};

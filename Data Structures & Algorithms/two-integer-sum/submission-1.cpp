#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> nums_seen;

        for(int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            auto num = nums_seen.find(complement);

            if (num != nums_seen.end()) {
                return {num->second, i};;
            } else {
                nums_seen[nums[i]] = i;
            }
        }
        return {};
    }
};

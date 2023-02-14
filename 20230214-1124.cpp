#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


class Solution {
public:
    int longestWPI(vector<int>& hours) {
        int n = hours.size();
        unordered_map<int, int> ump;
        int s = 0, res = 0;
        for (int i = 0; i < n; i++) {
            s += hours[i] > 8 ? 1 : -1;
            if (s > 0) {
                res = max(res, i + 1);
            } else {
                if (ump.count(s - 1)) {
                    res = max(res, i - ump[s - 1]);
                }
            }
            if (!ump.count(s)) {
                ump[s] = i;
            }
        }
        return res;
    }
};

int main() {
    Solution sol = Solution();
    std::vector<int> amount = {6,6,9};
    int res = sol.longestWPI(amount);
    std::cout<< res << std::endl;
}

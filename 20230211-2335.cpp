#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

class Solution {
public:
    int fillCups(vector<int>& amount) {
        sort(amount.begin(), amount.end());
        if (amount[2] >= amount[0] + amount[1]) {
            return amount[2];
        } else {
            int remains = amount[0] + amount[1] - amount[2];
            if (remains % 2 == 0) {
                return amount[2] + remains / 2;
            } else {
                return amount[2] + remains / 2 + 1;
            }
        }
    }
};

int main() {
    Solution sol = Solution();
    std::vector<int> amount = {5, 4, 4};
    int res = sol.fillCups(amount);
    std::cout<< res << std::endl;
}
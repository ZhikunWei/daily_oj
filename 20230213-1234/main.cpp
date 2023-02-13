#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
using namespace std;


class Solution {
public:
    int balancedString(string s) {
        int q_num = 0; int w_num = 0; int e_num = 0; int r_num = 0;
        for (auto c : s) {
            q_num += c == 'Q';
            w_num += c == 'W';
            e_num += c == 'E';
            r_num += c == 'R';
        }
        int result = s.size();
        const int avg = s.size() / 4;
        int left = 0; int right = 0;
        while (q_num > avg || w_num > avg || e_num > avg || r_num > avg) {
            q_num -= s[right] == 'Q';
            w_num -= s[right] == 'W';
            e_num -= s[right] == 'E';
            r_num -= s[right] == 'R';
            right++;
        }
        result = min(result, right - left);
        cout<<left<<", "<<right << " "<< string(s.begin()+left, s.begin() + right) << " " <<q_num << " " <<w_num << " "<<e_num << " "<<r_num << " "<<endl;
        while (left < s.size() && right < s.size()) {
            q_num += s[left] == 'Q';
            w_num += s[left] == 'W';
            e_num += s[left] == 'E';
            r_num += s[left] == 'R';
            left++;
            while ((q_num > avg || w_num > avg || e_num > avg || r_num > avg) && right < s.size()) {
                q_num -= s[right] == 'Q';
                w_num -= s[right] == 'W';
                e_num -= s[right] == 'E';
                r_num -= s[right] == 'R';
                right++;
            }
            cout<<left<<", "<<right << " "<< string(s.begin()+left, s.begin() + right)<< " " <<q_num << " " <<w_num << " "<<e_num << " "<<r_num << " "<<endl;
            result = min(result, right - left);
        }
        while (left < s.size() && (q_num <= avg && w_num <= avg && e_num <= avg && r_num <= avg)) {
            result = min(result, right - left);
            q_num += s[left] == 'Q';
            w_num += s[left] == 'W';
            e_num += s[left] == 'E';
            r_num += s[left] == 'R';
            left++;
            cout<<left<<", "<<right << " "<< string(s.begin()+left, s.begin() + right)<< " " <<q_num << " " <<w_num << " "<<e_num << " "<<r_num << " "<<endl;
        }
        return result;
    }
};

int main() {
    Solution sol = Solution();
    string s = "WQWRQQQW";
    int res = sol.balancedString(s);
    std::cout<< res << std::endl;
}
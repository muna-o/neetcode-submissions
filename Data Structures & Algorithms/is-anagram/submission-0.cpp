class Solution {
public:
    bool isAnagram(string s, string t) {
        int count[26];

        for (char c : s) {
            count[c - 'a']++;
        }
        
        for (char c : t) {
            count[c - 'a']--;
        }

        for (int entry : count) {
            if (entry != 0) {
                return false;
            }
        }
        return true;
    }
};

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {

        string referenceString = strs[0];

        for (int i = 0; i < static_cast<int>(referenceString.length()); i++) {
            for (string s : strs) {
                if (s[i] != referenceString[i]) {
                    return referenceString.substr(0, i);
                }
            }
        }

        return referenceString;
        
    }
};
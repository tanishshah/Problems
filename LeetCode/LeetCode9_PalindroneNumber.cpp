//Tanish Shah

//Leet code 9
//https://leetcode.com/problems/palindrome-number

class Solution {
public:
    bool isPalindrome(int x) {
        string y = to_string(x);
        int i = 0;
        int j = (int) y.length() - 1;
        while(i < j)
        {
            if(y[i] !=y[j])
                return false;
            i++;
            j--;
        }
        return true;
    }
};
//Tanish Shah

//LeetCode 7
//https://leetcode.com/problems/reverse-integer/

class Solution {
public:
    int reverse(int x) {
        long z =0;
        bool neg = false;
        if (x < 0)
            neg = true;
        z = abs(x);
        string y = to_string(z);
        int j= (int) y.length() - 1;
        int i = 0;
        while(i<j)
        {
            char temp = y[i];
            y[i] = y[j];
            y[j] = temp;
            i++;
            j--;
        }
        z = stol(y);
        if(neg == true)
            z = z*-1;
        if(z > pow(2,31) -1 || z <pow(-2,31))
            return 0;
        z = (int) z;
        return z;
    }
};
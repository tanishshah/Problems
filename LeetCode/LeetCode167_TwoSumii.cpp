//Tanish Shah
//https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        bool cont = true;
        vector<int> v;
        int i = 0;
        int j = numbers.size()-1;
        while(cont)
        {
            if(numbers[i]+numbers[j]==target)
            {
                v.push_back(i+1);
                v.push_back(j+1);
                cont = false;
            }
            else if(numbers[i]+numbers[j]>target)
                j--;
            else if(numbers[i]+numbers[j]<target)
                i++;
            else if(i<j)
                cont = false;
        } 
        return v;
    }
};
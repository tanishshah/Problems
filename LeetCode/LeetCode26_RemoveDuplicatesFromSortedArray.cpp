//Tanish Shah

//https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int unique = 0;
        int count = 0;
        if(nums.empty())
        {
            return 0;
        }
        for(int i = 0; i<nums.size();i++)
        {
            if(i == 0)
            {
                unique = nums[i];
            }
            else if(nums[i] != unique)
            {
                count++;
                unique = nums[i];
                nums[count]=unique;
            }
        }
        return count+1;
    }
};
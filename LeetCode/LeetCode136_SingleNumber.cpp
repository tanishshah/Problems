//Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int max = -999999;
        int min = 999999;
        for(int i = 0; i<nums.size();i++)
        {
            max = max<nums[i] ? nums[i]: max;
            min = min>nums[i]? nums[i]:min;
        }
        cout<<min<<endl;
        vector<int> pos(abs(max)+1,0);
        vector<int> neg(abs(min)+1,0);
        for(int i = 0;i<nums.size();i++)
        {
            if(nums[i]>0)
                pos[nums[i]]++;
            else
                neg[abs(nums[i])]++;
        }
        for(int i = 0;i<pos.size();i++)
        {
            if(pos[i] == 1)
                return i;
        }
        for(int i = 0; i<neg.size();i++)
        {
            if(neg[i] == 1)
                return -1*i;
        }
        return 0; //should never reach here
    }
};
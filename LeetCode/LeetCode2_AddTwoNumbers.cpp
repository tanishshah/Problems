//Tanish Shah

//LeetCode 2
//https://leetcode.com/problems/add-two-numbers

//Linear run time -> O(n)
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* l3 = NULL;
        vector<int>v;
        int add = 0;
        int sum = 0;
        while(l1!=NULL || l2!=NULL)
        {
            if(l1!=NULL && l2!=NULL)
            {
                sum = l1->val + l2->val + add;
                add = 0;
                v.push_back(sum%10);
                add = sum/10;
                l1 = l1->next;
                l2 = l2->next;
            }
            else if(l1!=NULL)
            {
                sum = l1->val + add;
                add = 0;
                v.push_back(sum%10);
                add = sum/10;
                l1 = l1->next;
            }
            else
            {
                sum = l2->val + add;
                add = 0;
                v.push_back(sum%10);
                add = sum/10;
                l2 = l2->next;
            }
            
        }
        if(add!=0)
        {
            v.push_back(add);
        }
        for(int i = v.size()-1;i>-1;i--)
        {
            ListNode* temp = new ListNode;
            temp -> val = v[i];
            temp ->next = l3;
            l3 =temp;
        }
        
        return l3;
    }
};
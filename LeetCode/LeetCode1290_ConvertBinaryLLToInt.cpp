//Tanish Shah

//LeetCode1290
//https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

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
    vector<int> v;
    
    int getDecimalValue(ListNode* head) {
    while(head!=NULL)
    {
        v.push_back(head->val);
        head = head->next;
    }
    int s = v.size()-1;
    int num = 0;
    for(int i =0; i<v.size();i++)
    {
        num+= v[i]*(pow(2,s));
        s--;
    }
    return num;
    }
};
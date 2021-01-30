//Tanish Shah

//LeetCode 203
// 
//https://leetcode.com/problems/remove-linked-list-elements/

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
    ListNode* removeElements(ListNode* head, int val) {
        stack<int>s;
        ListNode* removed = NULL;
        while(head!=NULL)
        {
            if(head->val != val)
                s.push(head->val);
            head =head->next;
        }

        while(!s.empty())
        {
            ListNode* temp = new ListNode();
            temp -> val = s.top();
            temp ->next = removed;
            removed = temp;
            s.pop();
        }
        return removed;

    }
};
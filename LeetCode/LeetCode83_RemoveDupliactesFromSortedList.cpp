//Tanish Shah

//LeetCode 83
//https://leetcode.com/problems/remove-duplicates-from-sorted-list/

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
    ListNode* deleteDuplicates(ListNode* head) {
        if(!head)
            return head;
        else if(!head->next)
            return head;
        int val = head->val;
        ListNode* temp = head->next;
        ListNode* cur = head->next;
        ListNode* prev = head;
        while(cur)
        {
            if(cur->val==val)
            {
                cur=cur->next;
                prev->next=cur;
                temp=nullptr;
                delete temp;
                temp = cur;
            }
            else
            {
                val = cur->val;
                cur=cur->next;
                temp=temp->next;
                prev=prev->next;
            }
        }
        return head;
    }
};
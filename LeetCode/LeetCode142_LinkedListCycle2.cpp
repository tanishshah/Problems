//Tanish Shah

//LeetCode 142
//https://leetcode.com/problems/linked-list-cycle-ii/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        if(!head)
            return head;
        ListNode* bunny = head;
        ListNode* turtle = head;
        ListNode* sloth = head;
        bool found = false;
        while(bunny)
        {
            if(bunny->next)
                bunny=bunny->next->next;
            else
                bunny=bunny->next;
            turtle=turtle->next;
            if(bunny == sloth || turtle == sloth)
            {
                found = true;
                break;
            }
            else if(bunny==turtle)
            {
                sloth=sloth->next;
            }
        }
        if(!found)
            return nullptr;
        return sloth;
    }
};
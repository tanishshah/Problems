
/*
Given the head of a linked list, remove the nth node from the end of the list and return its head.
    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz
*/

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
//non one pass attempt
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if(!head->next && n == 1)
        {
            head=nullptr;
            return head;
        }
        ListNode* temp = head;
        int length = 0;
        int count = 1;
        while(temp)
        {
            length++;
            temp = temp->next;
        }
        temp = head;
        if(count>length-n)
        {
            temp = head->next;
            head = nullptr;
            head = temp;
            return head;
        }
        while(count<length - n)
        {
            temp = temp->next;
            count++;
        }

        ListNode* temp2 = temp->next;
        if(temp2->next)
            temp->next = temp2->next;
        else
            temp->next = nullptr;
        temp2= nullptr;
        delete temp2;
        return head;
    }
};
//Tanish Shah

//LeetCode206
//https://leetcode.com/problems/reverse-linked-list/

//Iterative approach
//O(N)

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
    ListNode* reverseList(ListNode* head) {
        if(!head) //no list
            return head;
        else if(!head->next) //only head
            return head;
        else{
            ListNode* temp = head;
            ListNode* cur = head;
            ListNode* temp2 = head->next;
            while(temp2)
            {
               if(cur == head)
                   cur->next = nullptr;
                cur = temp2;
                temp2=temp2->next;
                cur->next = temp;
                temp = cur;
            }
            head = cur;
        }
        return head;
    }
};
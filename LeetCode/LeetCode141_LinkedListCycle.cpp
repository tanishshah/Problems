//Tanish Shah

//LeetCode 141
//https://leetcode.com/problems/linked-list-cycle

//Floyd's algorithm approach
//O(N) run time

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
    bool hasCycle(ListNode *head) {
        bool cycle = false;
        if(!head)
            return cycle;
        else if(!head->next)
            return cycle;
        else{
            ListNode* turtle = head;
            ListNode* rabbit = head;
            while(rabbit && !cycle)
            {
                if(rabbit->next)
                    rabbit = rabbit->next->next;
                else
                    rabbit = rabbit->next;
                turtle = turtle->next;
                if(rabbit == turtle)
                    cycle = true; 
            }
        }
        return cycle;
    }
};
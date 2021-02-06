//Tanish Shah

//lc 876
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
    ListNode* middleNode(ListNode* head) {
        if(!head)
            return head;
        if(!head->next)
            return head;
        int count = 0;
        ListNode* temp = head;
        while(temp)
        {
            count++;
            temp=temp->next;
        }
        temp = head;
        count/=2;
        for(int i = 0;i<count;i++)
            temp = temp->next;
        return temp;
    }
};
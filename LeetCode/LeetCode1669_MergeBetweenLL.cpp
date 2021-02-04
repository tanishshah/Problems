//Tanish Shah

//Leetcode 1669
//https://leetcode.com/problems/merge-in-between-linked-lists/

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
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        if(!list1 && !list2)
            return list1;
        else if(!list1)
            return list2;
        else if(!list2)
            return list1;
        ListNode* cur = list1;
        ListNode* temp = list1;
        ListNode* temp2 = list1->next;
        ListNode* cur2 = list2;
        int nNum = 1;
        while(nNum<a && cur)
        {
            cur=cur->next;
            nNum++;
        }
        temp2=cur->next;
        temp = cur;
        while(nNum<=b)
        {
            temp = temp2;
            if(temp2)
                temp2=temp2->next;
            temp =nullptr;
            delete temp;
            cur->next = temp2;
            temp = cur;
            nNum++;
        }
        while(cur2->next)
            cur2=cur2->next;
        cur2->next=temp2;
        cur->next = list2;
        return list1;
    }
};
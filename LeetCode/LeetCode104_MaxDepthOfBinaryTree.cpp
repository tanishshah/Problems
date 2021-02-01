//Tanish Shah
//https://leetcode.com/problems/maximum-depth-of-binary-tree/


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void traverse(TreeNode* root,int &max, int &cur) 
    {
        if (!root)
        {
            cur-=1;
            if(cur>max)
                max=cur;
            return;
        }
        traverse(root->left,max,cur+=1);
        traverse(root->right,max,cur+=1);
        cur-=1;
    }
    int maxDepth(TreeNode* root) {
        if(!root)
            return 0;
        int max =1, cur=1;
        traverse(root,max,cur);
        return max;
    }
};
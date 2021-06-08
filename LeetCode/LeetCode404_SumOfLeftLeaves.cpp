//Given the root of a binary tree, return the sum of all left leaves.

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
    int sumOfLeftLeaves(TreeNode* root) {
        int value = 0;
        if(!root)
            return 0;
        if(root->left)
        {
            if(!root->left->left && !root->left->right)
                value += root->left->val;
        }
        value+=sumOfLeftLeaves(root->left);
        value+=sumOfLeftLeaves(root->right);
        return value;
    }
};
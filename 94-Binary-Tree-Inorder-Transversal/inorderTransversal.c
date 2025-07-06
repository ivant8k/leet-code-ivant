/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

// Helper function for inorder traversal
void inorderHelper(struct TreeNode* root, int* result, int* idx) {
    if (root == NULL) return;
    inorderHelper(root->left, result, idx);
    result[(*idx)++] = root->val;
    inorderHelper(root->right, result, idx);
}

int* inorderTraversal(struct TreeNode* root, int* returnSize) {
    int* result = (int*)malloc(100 * sizeof(int));
    int idx = 0;
    inorderHelper(root, result, &idx);
    *returnSize = idx;
    return result;
}

int main() {
    // Example usage of inorderTraversal
    struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    root->val = 1;
    root->left = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    root->left->val = 2;
    root->right = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    root->right->val = 3;

    int returnSize = 0;
    int* result = inorderTraversal(root, &returnSize);

    for (int i = 0; i < returnSize; i++) {
        printf("%d ", result[i]);
    }
    printf("\n");

    // Free allocated memory
    free(result);
    free(root->left);
    free(root->right);
    free(root);

    return 0;
}
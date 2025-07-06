#include <stdio.h>

void sortColors(int* nums, int numsSize);

void sortColors(int* nums, int numsSize) {
    for (int i = 0, j = 0, k = numsSize - 1; j <= k;) {
        if (nums[j] == 0) {
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
            i++;
            j++;
        } else if (nums[j] == 1) {
            j++;
        } else {
            int temp = nums[j];
            nums[j] = nums[k];
            nums[k] = temp;
            k--;
        }
    }
}


int main() {
    int nums[] = {2, 0, 2, 1, 1, 0};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    sortColors(nums, numsSize);
    for (int i = 0; i < numsSize; i++) {
        printf("%d ", nums[i]);
    }
    printf("\n");
    return 0;
}
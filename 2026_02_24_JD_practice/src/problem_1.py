"""❓ Problem
Given an array and target K, return True if two numbers sum to K.

> Example:
Input: [2, 7, 11, 15], K = 9
Output: True
"""
from operator import indexOf

def two_sum(arr, K):
    seen = set()

    for num in arr:
        if K - num in seen:
            return True
        seen.add(num)

    return False

def two_sumx (nums, k) -> bool:
    seen = set()
    for num in nums:
        if k-num in seen:
            return True
        seen.add()
"""
> set is fast and memeory efficient.
set has no index. values are direct hashed location in RAM
setting empty set in python: x = set()
and example of set: x = {1,3,5}
> idx, val in enumerate(itr, start=)
"""
def is_match(nums, k)-> bool:
    for i in range(len(nums)):
        initial: int = nums[i]
        need_more: int = k - initial

        for idx, num in enumerate(nums):
            if i == idx:
                continue
            if need_more == num:
                print(f"Yes match found: {initial}+{need_more}={k}")
                return True
    else:
        return False

if __name__ == "__main__":
    numbers: int = [2,7,11,15]
    target_k: int = 26
    result: bool = is_match(numbers, target_k)
    print(result)
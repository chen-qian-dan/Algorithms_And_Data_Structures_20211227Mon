"""
Leetcode:
384. Shuffle an Array

Given an integer array nums, design an algorithm to randomly shuffle the array. All permutations of the array should be equally likely as a result of the shuffling.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the integer array nums.
int[] reset() Resets the array to its original configuration and returns it.
int[] shuffle() Returns a random shuffling of the array.
"""

from typing import List 
import random 

class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums[:]
        self.nums = nums 
        

    def reset(self) -> List[int]:
        self.nums = self.original[:]
        return self.nums 
        

    def shuffle(self) -> List[int]:
        """
        because del tmp[r] is O(N^2)
        so, need to improve this part
        Fisher-Yates Shuffle: time O(N), space O(N)
        """
        for i in range(len(self.nums)):
            r = random.randrange(i, len(self.nums))
            self.nums[i], self.nums[r] = self.nums[r], self.nums[i]
        return self.nums
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
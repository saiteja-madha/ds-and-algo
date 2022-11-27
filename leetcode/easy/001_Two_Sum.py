# Two Sum
# https://leetcode.com/problems/two-sum/

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

def twoSum(nums: list[int], target: int):
    map = {}
    for i, num in enumerate(nums):
        req = target - num
        if req in map:
            return [map[req], i]
        map[num] = i


nums = [3, 2, 4]
target = 6

print(twoSum(nums, target))

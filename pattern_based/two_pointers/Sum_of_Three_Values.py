# https://www.educative.io/courses/grokking-coding-interview-patterns-python/sum-of-three-values


def find_sum_of_three(nums, target):
    if len(nums) < 3:
        return False
    if len(nums) == 3:
        return nums[0] + nums[1] + nums[2] == target
    nums.sort()
    for i in range(len(nums) - 1, 1, -1):
        cur = nums[i]
        l, r = 0, i - 1
        rem = target - cur
        while l < r:
            cal = nums[l] + nums[r]
            if cal == rem:
                return True
            if cal > rem:
                r -= 1
            else:
                l += 1
    return False


nums = [1, -1, 0]
target = -1
assert find_sum_of_three(nums, target) is False

nums = [3, 7, 1, 2, 8, 4, 5]
target = 10
assert find_sum_of_three(nums, target) is True

nums = [3, 7, 1, 2, 8, 4, 5]
target = 21
assert find_sum_of_three(nums, target) is False

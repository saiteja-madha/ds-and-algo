# https://leetcode.com/problems/happy-number/


class Solution:

    # Using Set
    # O(n) - Space
    # def isHappy(self, n: int) -> bool:
    #     seen=set()
    #     while(n != 1 and n not in seen):
    #         seen.add(n)
    #         n=sum(int(i)**2 for i in str(n))
    #     return n == 1

    # Fast pointer
    def isHappy(self, n: int) -> bool:
        def sq_sum(num):
            return sum(int(digit) ** 2 for digit in str(num))

        slow = fast = n
        while True:
            slow = sq_sum(slow)
            fast = sq_sum(sq_sum(fast))
            if fast == 1 or slow == fast:
                break

        return fast == 1


# Example 1:
n = 19
assert Solution().isHappy(n) is True

# Example 2:
n = 2
assert Solution().isHappy(n) is False

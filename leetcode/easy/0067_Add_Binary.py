# https://leetcode.com/problems/add-binary/

# Given two binary strings a and b, return their sum as a binary string.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        diff = abs(len(a) - len(b))
        a = ("0" * diff + a) if (len(a) < len(b)) else a
        b = ("0" * diff + b) if (len(b) < len(a)) else b

        carry = 0
        res = []
        for i in range(len(a)-1, -1, -1):
            bit1, bit2 = int(a[i]), int(b[i])
            currBit = (bit1 + bit2 + carry) % 2
            carry = (bit1 + bit2 + carry)//2
            res.append(str(currBit))
        if carry:
            res.append(str(carry))
        return "".join(res)[::-1]


print(Solution().addBinary("11", "1"))  # "100"
print(Solution().addBinary("1010", "1011"))  # "10101"

import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if concatenating in both orders gives the same result
        if str1 + str2 != str2 + str1:
            return ""

        # Find the greatest common divisor of lengths
        gcd_length = math.gcd(len(str1), len(str2))

        # Return the prefix of str1 up to the gcd length
        return str1[:gcd_length]


sol = Solution()
print(sol.gcdOfStrings("ABCABC", "ABC"))
print(sol.gcdOfStrings("ABABAB", "ABAB"))
print(sol.gcdOfStrings("LEET", "CODE"))

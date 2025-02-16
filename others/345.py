class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        s_list = list(s)
        left = 0
        right = len(s_list) - 1

        while left < right:
            if s_list[left] not in vowels:
                left += 1
                continue
            if s_list[right] not in vowels:
                right -= 1
                continue

            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1

        return "".join(s_list)


sol = Solution()
print(sol.reverseVowels("IceCreAm"))

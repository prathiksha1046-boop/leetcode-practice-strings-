class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = "aeiouAEIOU"
        mid = len(s)//2

        a = s[:mid]
        b = s[mid:]

        count_a = 0
        count_b = 0

        for ch in a:
            if ch in vowels:
                count_a += 1

        for ch in b:
            if ch in vowels:
                count_b += 1

        return count_a == count_b
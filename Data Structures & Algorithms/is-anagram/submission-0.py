class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters = [0] * 26

        for schar in s:
            letters[ord(schar) - ord('a')] += 1

        for tchar in t:
            letters[ord(tchar) - ord('a')] -= 1

        for letter in letters:
            if letter != 0:
                return False

        return True
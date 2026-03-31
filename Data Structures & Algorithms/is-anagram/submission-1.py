# Approach
# As we already know we letters are lowercase so we credted list of size 26 and added 0 by default
# loop both words.

# Time complexity is O(n) an dspace O(1)

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
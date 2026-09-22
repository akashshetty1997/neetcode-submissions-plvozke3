# Valid Anagram

# i will check if both length are same if its different i will return false. i will take first string loop it and make a hashmap where key is each item in the string and increment a count if i find double exmaple "racecar" { r = 2, a = 2, c = 2, e = 1 } then i will loop another string try to find that wrod is there in hasmap if not then return false if there then decrement in the hashmap should be empty then it valid Anagram

# issue is its space complexity will be O(nm) where both n and m are two strings

# psace is O(n) because s and t consist of lowercase English letters.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        new_s = {}

        if len(s) != len(t):
            return False

        for char in s:
            if char in new_s:
                new_s[char] += 1
            else:
                new_s[char] = 1

        for char in t:
            if char in new_s:
                new_s[char] -= 1
            else:
                return False

        for char in new_s:
            if new_s[char] != 0:
                return False

        return True
        
# Approach -
# I am using dictionary  here and keeping value as default list.
# we loop through words array and then loop each word we create empty list of size 26 default 0,
# then we create unique key using letters as we alreayd know the input gonna be lowercase so gonna be 97 to 122 
# in ascii.  then we chekc if it present in dict if not then create it and append the word.

# Time complexity = O(n * k) here n is the strs for loop and then k is the each letter loop.
# Space complexity = O(n * k)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_strs = defaultdict(list)

        for word in strs:
            key = [0] * 26
            for c in word:
                key[ord(c) - ord('a')] += 1
            new_strs[tuple(key)].append(word)

        return list(new_strs.values())
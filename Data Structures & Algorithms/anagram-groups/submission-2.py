
# # first i will create a empty dict. loop the strs get a first element example "act" convert string into ascii for that we need to loop the charcter like a inner loop 7 + 99 + 116 = 312. we add key 321 and vlaue a array ["act"] we insert if there is no key 321 if ther is a key named 321 we push thsi string insde the value.

# #space complexity is O(nm) where n is loopig strs and m in looping each strs
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         group_anagrams = {}
#         results = []
#         if len(strs) != 0:
#             for str in strs:
#                 total_char = 0
#                 for char in str:
#                     total_char += ord(char)
#                 if total_char in group_anagrams:
#                     # group_anagrams[total_char].push(str)
#                      group_anagrams[total_char].insert(0, str)
#                 else:
#                     group_anagrams[total_char] = [str]
            
#             for item in group_anagrams:
#                 # results.push(item)
#                 results.insert(0, item)
#             return results
#         else:
#             return [[""]]


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = {}

        for word in strs:
            count = [0] * 26

            for char in word:
                index = ord(char) - ord('a')
                count[index] += 1

            key = tuple(count)

            if key in group_anagrams:
                group_anagrams[key].append(word)
            else:
                group_anagrams[key] = [word]

        return list(group_anagrams.values())
        
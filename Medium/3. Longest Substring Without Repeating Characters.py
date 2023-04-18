class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lst = []
        count = 0
        maximum = 0

        for num in range(len(s)):
            elem = s[num]
            if elem in lst:
                if count > maximum:
                    maximum = count
                if elem == s[num - 1]:
                    lst = [elem]
                    count = 1
                else:
                    for _ in range(lst.index(elem) + 1):
                        lst.remove(lst[0])
                        count -= 1
                    lst.append(elem)
                    count += 1
            else:
                lst.append(elem)
                count += 1

        if count > maximum:
            maximum = count
        return maximum
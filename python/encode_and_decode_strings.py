class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, str):
        res, i = [], 0

        while i < len(str):
            j = i
            while str[j] != '#':
                j += 1
            length = int(str[i:j])
            res.append(str[j + 1:j + 1 + length])
            i = j + 1 + length
        return res


tmp = Solution
print(tmp.encode(tmp, ["a", "bc", "def"]))
print(tmp.decode(tmp, "1#a2#bc3#def"))

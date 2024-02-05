class Solution(object):
    def isAnagram(self, s, t):
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        for c in t:
            if c in d and d[c] > 0:
                d[c] -= 1
                if not d[c]:
                    del d[c]
            else:
                return False

        if d:
            return False
        else:
            return True


test_cases = {
    ('anagram', 'nagaram'): True,
    ('car', 'rat'): False,
    ('a', 'a'): True,
    ('a', 'b'): False,
    ('ab', 'ba'): True,
    ('aab', 'aba'): True,
    ('aa', 'a'): False,
    ('a', 'aa'): False
}

s = Solution()

for test_case, res in test_cases.items():
    assert s.isAnagram(test_case[0], test_case[1]) == res, (test_case, s.isAnagram(test_case[0], test_case[1]))
class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()
        if len(pattern) != len(words):
            return False

        pattern_dict = {}
        for letter, word in zip(pattern, words):
            if letter in pattern_dict:
                if pattern_dict[letter] != word:
                    return False
            else:
                if word in pattern_dict.values():
                    return False
                pattern_dict[letter] = word

        return True


test_cases = {
    ('abba', 'dog cat cat dog'): True,
    ('abba', 'dog cat cat fish'): False,
    ('aaa', 'dog g g'): False,
    ('abba', 'a a a a'): False
}

sol = Solution()

for test_case, test_res in test_cases.items():
    pattern, s = test_case
    res = sol.wordPattern(pattern, s)
    assert res == test_res, (test_case, res)


class Solution(object):
    def isPowerOfTwo(self, n):

        if n == 0:
            return False

        if n == 1:
            return True

        bytes_string = str(bin(n))[2:]

        first_bit = bytes_string[0]
        other_bits = bytes_string[1:]

        if first_bit and all((bit == '0' for bit in other_bits)):
            return True

        return False


test_cases = {
    0: False,
    1: True,
    2: True,
    3: False,
    4: True,
    5: False,
    8: True,
    10: False,
    2 ** 10: True
}


s = Solution()

for test_case, res in test_cases.items():
    assert s.isPowerOfTwo(test_case) == res, (test_case, s.isPowerOfTwo(test_case))

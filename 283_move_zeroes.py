class Solution(object):
    def moveZeroes(self, nums):
        if len(nums) <= 1:
            return nums

        zeroes_batch = 0

        for i in range(len(nums)):
            el = nums[i]
            if el == 0:
                if i < len(nums) - 1:
                    if nums[i+1] != 0:
                        nums[i - zeroes_batch] = nums[i + 1]
                        nums[i + 1] = 0
                    else:
                        zeroes_batch += 1




test_cases = {
    (0, 1, 2): [1, 2, 0],
    (0, 1, 0, 2): [1, 2, 0, 0],
    tuple(): [],
    (0, ): [0],
    (1, ): [1],
    (0, 1): [1, 0],
    (1, 0): [1, 0],
}


s = Solution()

for test_case, res in test_cases.items():
    l = list(test_case)
    s.moveZeroes(l)
    assert l == res, (test_case, l)
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        if self.nums:
            left = min(left, len(self.nums))
            right = min(right+1, len(self.nums))
        return sum(self.nums[left:right])


nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)

param_1 = obj.sumRange(0, 2)
param_2 = obj.sumRange(2, 5)
param_3 = obj.sumRange(0, 5)

print(param_1, param_2, param_3)

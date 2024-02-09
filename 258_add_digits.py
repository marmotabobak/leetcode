class Solution(object):
    def addDigits(self, num: str):
        if int(num) < 10:
            return num
        else:
            total = sum(map(int, str(num)))
            return self.addDigits(total)

def isBadVersion(version):
    if version <= 3:
        return False
    else:
        return True


class Solution(object):
    def firstBadVersion(self, n):

        if n == 1:
            return 1

        l = 1
        r = n

        while l <= r:
            mid = (l + r) // 2

            if isBadVersion(mid):
                r = mid - 1
            else:
                last_true_version = mid
                l = mid + 1

        return l


s = Solution()
print(s.firstBadVersion(10))
class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst = list(s)
        lst = [ord(letter) for letter in lst]
        acm = 0
        for l in range(len(lst)-1):
            acm += abs(lst[l] - lst[l+1])
        return acm

acm = Solution().scoreOfString("zaz")
print(acm)
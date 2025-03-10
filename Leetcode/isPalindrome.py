class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        n_str = str(x)
        r = n_str[::-1]
        n = int(r)

        if x == n:
            return True
        return False

list = [121, 424, 123, 321, -123, 444, -1, 1]

for item in list:
    print(item)
    print(Solution.isPalindrome(Solution(), item))
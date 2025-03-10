class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return None
        
        r = list(s)
        print(r)
        print(len(r))
        c = [] #list converted to number

        #convert to number
        for l in range (0, len(r)):
            if r[l] == 'I':
                c.append(1)
            if r[l] == 'V':
                c.append(5)
            if r[l] == 'X':
                c.append(10)
            if r[l] == 'L':
                c.append(50)
            if r[l] == 'C':
                c.append(100)
            if r[l] == 'D':
                c.append(500)
            if r[l] == 'M':
                c.append(1000)

        print(c)
        n: int = 0
        p: int = 0 #pointer

        while len(c)-1 > p:

            l = p
            l1 = l + 1
            l2 = l + 2

            if c[l] == c[l1]:
                n = c[l] + c[l1]
                print("n", n)
                p = l1 + 1 

                if c[l1] == c[l2]:
                    n = n + c[l2]
                    print("n", n)
                    p = l2 + 1
                else: 
                    p = l1 + 1

            if c[l] > c[l1]:
                n = c[l] + c[l1]

            if c[l] < c[l1]:
                n = c[l1] - c[l]

        print(n)

Solution().romanToInt('II')
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if(x == 0):
            return 0
        flag = 0
        s = list(str(x))
        l = len(str(x))
        first = s[0]
        last = s[l - 1]
        if(first == '-'):
            s.pop(0)
            flag = 1
            l = l - 1
        if(last == '0'):
            s.pop(l - 1)

        s.reverse()

        rstr = -int("".join(s)) if(flag) else int("".join(s))
        if(rstr >= -2147483648 and rstr <= 2147483647):
            return rstr
        else:
            return 0


s = Solution()
print(s.reverse(1534236469))

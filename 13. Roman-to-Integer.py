class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        arr = list(s)
        tmp = 0
        sum = 0
        i = 0
        while i < len(s):
            if(i < len(s) - 1):
                if(arr[i] == 'I' or arr[i] == 'X' or arr[i] == 'C'):
                    tmp = self.twoNum(arr[i] + arr[i + 1])
                    if(tmp == 0):
                        sum = sum + dic[arr[i]]
                        i = i + 1
                    else:
                        sum = sum + tmp
                        i = i + 2
                else:
                    sum = sum + dic[arr[i]]
                    i = i + 1
            else:
                sum = sum + dic[arr[i]]
                i = i + 1
        return sum

    def twoNum(self, s):
        n = 0
        if(s == 'IV'):
            n = 4
        elif(s == 'IX'):
            n = 9
        elif(s == 'XL'):
            n = 40
        elif(s == 'XC'):
            n = 90
        elif(s == 'CD'):
            n = 400
        elif(s == 'CM'):
            n = 900
        return n


s = Solution()
print(s.romanToInt('III'))
print(s.romanToInt('IV'))
print(s.romanToInt('IX'))

print(s.romanToInt('LVIII'))
print(s.romanToInt('MCMXCIV'))

class Solution:
    def intToRoman(self, num: int) -> str:
        string = ""
        M = num // 1000
        num = num % 1000
        C = num // 100
        num = num % 100
        X = num // 10
        I = num % 10
        string += "M" * M
        if C >= 5:
            string += "D" + "C" * (C - 5)
        else:
            string += "C" * C

        if X >= 5:
            string += "L" + "X" * (X - 5)
        else:
            string += "X" * X

        if I >= 5:
            string += "V" + "I" * (I - 5)
        else:
            string += "I" * I



        s = string.replace("DCCCC", "CM").replace("CCCC", "CD").replace("LXXXX", "XC").replace("XXXX", "XL").replace("VIIII", "IX").replace("IIII", "IV")

        return s
# Author: Elias Kalphat-Losego
# Description: Takes string and pattern (p).
# If the pattern matches the string return True otherwise return False.
# Return type is Boolean.


def Patternmatch(string, p):
    m = len(p)
    n = len(string)
    for i in range(n - m + 1):
        j = 0
        while (j < m):
            if string[i + j] != p[j]:
                if p[j] != "?":
                    if p[j] != "*":
                        break
            j += 1
        if j == m:
            return True
    return False


if __name__ == '__main__':
    string = "“abcde"
    p = "abc"
    p2 = "ad"
    p3 = "*a?c*"
    p4 = "*"

    print(Patternmatch(string, p))
    print(Patternmatch(string, p2))
    print(Patternmatch(string, p3))
    print(Patternmatch(string, p4))

# Author: Elias Kalphat-Losego
# Description: Given a string, find out if the string isak-palindrome or not.
# A k-palindrome string becomes a palindrome string when at most k characters
# are removed from the original string.
# Return True if the string is k-palindrome, else return False.
# Return type is Boolean.


def checkPalindrome_1(string, k):
    reverse_string = string[::-1]
    length = len(string)
    return checkPalindrome_1_helper(string, reverse_string, length, length) <= k * 2

def checkPalindrome_1_helper(string, reverse_string, m, n):
    if m == 0:
        return n
    if n == 0:
        return m
    if string[m - 1] == reverse_string[n - 1]:
        return checkPalindrome_1_helper(string, reverse_string, m - 1, n - 1)
    result = 1 + min(checkPalindrome_1_helper(string, reverse_string, m - 1, n),
                  (checkPalindrome_1_helper(string, reverse_string, m, n - 1)))
    return result

def checkPalindrome_2(string, k):
    reverse_string = string[::-1]
    length = len(string)
    return checkPalindrome_2_helper(string, reverse_string, length, length) <= k * 2

def checkPalindrome_2_helper(string, reverse_string, m, n):
    memo_table = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                memo_table[i][j] = j
            elif j == 0:
                memo_table[i][j] = i
            elif string[i - 1] == reverse_string[j - 1]:
                memo_table[i][j] = memo_table[i - 1][j - 1]
            else:
                memo_table[i][j] = 1 + min(memo_table[i - 1][j], memo_table[i][j - 1])
    return memo_table[m][n]


if __name__ == "__main__":
    string = "abcdcba"
    k = 1

    string2 = "abcdeba"
    k2 = 1

    print(checkPalindrome_1(string, k))
    print(checkPalindrome_1(string2, k2))

    print(checkPalindrome_2(string, k))
    print(checkPalindrome_2(string2, k2))
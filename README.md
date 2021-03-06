# Algorithms Portfolio Project
CS325 Analysis of Algorithms final project

# Purpose
This is a portfolio project for CS 325 - Analysis of Algorithms. There are two algorithms implemented in the included files. The first algorithm is meant to determine if a string is a k-palindrome. A k-palindrome is defined as any string that becomes a palindrome when any number of characters, k, are removed from the string. For example, the word "racecar" is a 0-palindrome because it is a palindrome if and only if no characters are removed from it. The string "abcbad" is a 1-palindrome because it may become a palindrome if one character, the "d" is removed from it.

The second algorithm compares two strings and determines if there is a pattern that exists between them. A string may contain asterisk or question-mark characters, where a question-mark may be substituted for any one character at the same index of the comparing string. An asterisk may be substituted for any number of characters at the same index of the comparing string. For example, the string "abcde" matches "abc" because it contains that string. 
The string "abcde" matches the strings "a?c" and "a*" because the question-mark is substituted for the character "b" at the same index, and the asterisk may replace any number of characters at the same index. However, strings "abcde" and "ad" do not match because the former does not contain the latter.

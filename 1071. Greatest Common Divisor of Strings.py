'''
For two strings s and t, we say "t divides s" if and only 
if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x 
such that x divides both str1 and str2.

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
'''

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        l1, l2 = len(str1), len(str2)
        
        if str1 + str2 != str2+str1: # если конкантинированные справа и слева строки не равны, то не будет вхождения одной строки в другую, возвращаем пустую строку
            return ''
        elif str1 == str2: # если строки равны - возвращаем одну из строк
            return str1
        elif l1 > l2: # если первая строка длинне второй, находим ее срез начиная с длины второй строки
            return self.gcdOfStrings(str1[l2:], str2)
        else: # если вторая строка длиннее, то находим срез по ней слева на длину первой строки
            return self.gcdOfStrings(str2[l1:], str1)
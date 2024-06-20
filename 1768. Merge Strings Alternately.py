'''
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
'''

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        w1_lst = list(word1)
        w2_lst = list(word2)

        n=1
        for i in range(0, len(w2_lst)):
            w1_lst.insert(i+n, w2_lst[i])
            n += 1
        return ''.join(w1_lst)

'''
1. Превращаем слова в списки
2. Проходимся циклом в диапозоне размера второго списка, в 1-й список вставляем символы из
второго списка, начиная с индекса 1, элементы списка 1 смещаются далее счетчик увеличиваем на 1 -
получается искомый список в шахматном порядке
3. Склеиваем стироку из полученного списка и возвращаем ее.
'''
'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
'''


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if list(str(x))[0] == '-':
            x_lst = list(str(x))[1:][::-1]
            x_reverse = -int(''.join(x_lst))
        else:
            x_lst = list(str(x))[::-1]
            x_reverse = int(''.join(x_lst))

        if x_reverse <= -2147483648 or x_reverse >= 2147483647:
            x_reverse = 0

        return x_reverse

'''
1. Проверяем было ли число отрицательным
2. Превращаем число в массив из символов и переворачиваем срезом
(если было отрицательным, то начиная с первого символа, если положительное, то с нулевого)
3. Склеиваем перевернутую строку и переводим в int
4. Если исходное число было отрицательным, то полученное число указываем с минусом
5. Проверяем не выходит ли полученное число за границы int32, если выходит - возвращаем ноль,
если нет, то возвращаем полученное число
'''
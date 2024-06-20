'''
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.
'''

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        return [i+extraCandies >= max(candies) for i in candies]

'''
Делаем простое списковое включение, проходимся по каждому элементу списка candies,
проверяем условие, что при добавлении к элементу списка extraCandies, оно становится  
>= максимума в исходном списке
'''
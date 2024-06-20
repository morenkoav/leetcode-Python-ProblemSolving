'''
Write a solution to list
the names of animals that weigh strictly more than 100 kilograms.
'''

mport pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals.weight > 100].sort_values(by=['weight'], ascending=False)[['name']]
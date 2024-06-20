'''
Write a solution to pivot the data so that each row represents temperatures for a specific month,
and each city is a separate column.
'''

import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    weather_pivot = pd.pivot_table(
        weather,
        values = 'temperature',
        index = 'month',
        columns = 'city'
    )
    return weather_pivot
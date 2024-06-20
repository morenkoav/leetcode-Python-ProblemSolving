'''
Write a solution to reshape the data so that each
row represents sales data for a product in a specific quarter.
'''

import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    report_pivot = pd.melt(report, id_vars=['product'], var_name='quarter', value_name='sales')
    return report_pivot
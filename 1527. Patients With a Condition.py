'''
Write a solution to find the patient_id, patient_name, and conditions 
of the patients who have Type I Diabetes. 
Type I Diabetes always starts with DIAB1 prefix.

Return the result table in any order.
'''

import pandas as pd
import re

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    regex = r'\bDIAB1+'
    patients['is_Diabet'] = patients['conditions'].apply(lambda x: re.search(regex, x))
    return patients[~patients.is_Diabet.isna()][['patient_id','patient_name','conditions']]
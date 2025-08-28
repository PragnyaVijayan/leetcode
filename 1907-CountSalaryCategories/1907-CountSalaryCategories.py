# Last updated: 8/27/2025, 11:40:58 PM
import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    unique_id_employees = pd.merge(employees, employee_uni, left_on='id', right_on='id', how='left')
    #print(unique_id_employees)
    return unique_id_employees[['unique_id', 'name']]
    
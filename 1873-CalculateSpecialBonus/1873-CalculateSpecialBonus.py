# Last updated: 8/23/2025, 12:03:54 AM
import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = 0
    condition = (employees['employee_id']%2==1) &  (~employees['name'].str.contains('M'))
    employees.loc[condition, 'bonus'] = employees.loc[condition, 'salary']

    return employees[['employee_id', 'bonus']].sort_values('employee_id')




    
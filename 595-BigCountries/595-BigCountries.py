# Last updated: 8/21/2025, 12:04:17 PM
import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(customers, orders, left_on='id', right_on='customerId', how='left')
    cust_wo_order = merged_df[merged_df['id_y'].isna()]
    cust_wo_order = cust_wo_order.rename(columns={'name': 'Customers'})
    return cust_wo_order[['Customers']]
    
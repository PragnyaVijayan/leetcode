# Last updated: 8/21/2025, 11:54:54 AM
import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:

    return products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')][['product_id']]
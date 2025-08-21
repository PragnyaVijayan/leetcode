# Last updated: 8/21/2025, 11:49:24 AM
import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    big = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)][['name', 'population', 'area']]
    #print(big.head())

    return big
    
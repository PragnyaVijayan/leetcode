# Last updated: 8/21/2025, 12:20:33 PM
import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    self_views = views[views['author_id'] == views['viewer_id']]
    result = self_views.groupby(['author_id']).first().reset_index()
    return result.rename(columns={'author_id': 'id'})[['id']]


    
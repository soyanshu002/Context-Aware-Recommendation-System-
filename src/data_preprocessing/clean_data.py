import pandas as pd

def clean_user_data(df: pd.DataFrame) -> pd.DataFrame:
    """Handle missing values, duplicates, and type conversions."""
    df = df.drop_duplicates()
    df = df.fillna({'location': 'unknown'})  # example
    return df

def clean_product_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean product catalog data."""
    df = df.drop_duplicates()
    df['price'] = df['price'].fillna(df['price'].median())
    return df

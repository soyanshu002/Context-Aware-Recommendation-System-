import pandas as pd
import os

def load_user_data(file_path: str) -> pd.DataFrame:
    """Load raw user interaction data."""
    return pd.read_csv(file_path)

def load_product_data(file_path: str) -> pd.DataFrame:
    """Load product catalog data."""
    return pd.read_csv(file_path)

def load_context_data(file_path: str) -> pd.DataFrame:
    """Load contextual information like time, location."""
    return pd.read_csv(file_path)

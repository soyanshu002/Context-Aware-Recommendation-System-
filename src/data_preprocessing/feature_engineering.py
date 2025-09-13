import pandas as pd

def add_time_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add features based on timestamp."""
    df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
    df['weekday'] = pd.to_datetime(df['timestamp']).dt.weekday
    return df

def encode_categorical(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """One-hot or label encode categorical features."""
    return pd.get_dummies(df, columns=columns)

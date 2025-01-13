import pandas as pd
from calculate_mean import calculate_mean


def load_data(file_path):
    df = pd.read_excel(file_path)
    data = pd.to_numeric(df.iloc[:, 0], errors='coerce').dropna().values
    return data




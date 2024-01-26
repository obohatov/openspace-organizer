import pandas as pd


def read_names_from_excel(filepath):
    """Read names from Excel file"""
    df = pd.read_excel(filepath)
    return df['name'].tolist()

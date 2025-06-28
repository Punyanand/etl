def transform_data(df):
    df = df.drop_duplicates()
    df.columns = [col.strip().lower() for col in df.columns]
    return df

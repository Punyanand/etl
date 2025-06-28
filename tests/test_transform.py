import pandas as pd
from etl.transform import transform_data

def test_transform_data():
    df = pd.DataFrame({
        "Name": ["Alice", "Bob", "Alice"],
        "Age": [30, 25, 30],
        "Country": ["USA", "Canada", "USA"]
    })
    result = transform_data(df)
    assert result.shape[0] == 2
    assert all(col in result.columns for col in ["name", "age", "country"])

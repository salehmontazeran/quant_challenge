import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv("HINDALCO_1D.csv")


def test_datetime(df):
    try:
        # Convert the datetime column to datetime format
        df["datetime"] = pd.to_datetime(df["datetime"], format="%Y-%m-%d %H:%M:%S")
    except:
        print("FAIL: datetime is in wrong format")


def test_close_high_low_open(df):
    try:
        # Convert the close, high, low, and open columns to decimal format
        df[["close", "high", "low", "open"]] = df[
            ["close", "high", "low", "open"]
        ].astype(float)

        # Check that the close, high, low, and open columns are of type float64 and Check for nan
        assert all(
            df[col].dtype == "float64" and not df[col].isnull().any()
            for col in ["close", "high", "low", "open"]
        )
    except:
        print("FAIL: First four column are not decimal")


def test_volume(df):
    try:
        # Convert the volume column to integer format
        df["volume"] = df["volume"].astype("Int64")

        # Check that the volume column is of type Int64 and check for nan
        assert df["volume"].dtype == "Int64" and not df["volume"].isnull().any()
    except:
        print("FAIL: Volume is not integer")


if __name__ == "__main__":
    test_datetime(df)
    test_close_high_low_open(df)
    test_volume(df)

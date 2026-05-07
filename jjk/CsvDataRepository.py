import pandas as pd
from pathlib import Path


class CsvDataRepository:
    def load(self, path: str) -> pd.DataFrame:
        file = Path(path)
        if not file.exists():
            raise FileNotFoundError
        return pd.read_csv(file)

    def load_required(self, path: str, required_columns: list) -> pd.DataFrame:
        df = self.load(path)
        for col in required_columns:
            if col not in df.columns:
                raise ValueError
        return df


if __name__ == "__main__":
    import os

    pd.DataFrame({
        "month": [1, 2, 3],
        "sales": [100, 150, 120]
    }).to_csv("sample.csv", index=False)

    repo = CsvDataRepository()

    df = repo.load("sample.csv")
    print("Loaded:")
    print(df)

    df2 = repo.load_required("sample.csv", required_columns=["month", "sales"])
    print("Loaded with required columns:")
    print(df2)

    os.remove("sample.csv")
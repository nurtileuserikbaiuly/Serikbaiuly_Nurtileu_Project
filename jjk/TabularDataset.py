import pandas as pd

class TabularDataset:

    def __init__(self, data):
        if isinstance(data, pd.DataFrame):
            self._df = data.copy()
        else:
            self._df = pd.DataFrame(data).copy()

    @property
    def data(self) -> pd.DataFrame:
        return self._df.copy()

    @property
    def shape(self) -> tuple:
        return self._df.shape

    @property
    def column_names(self) -> list:
        return list(self._df.columns)

    def head_info(self, n: int = 5) -> str:
        return str(self._df.head(n))

    def numeric_summary(self) -> pd.DataFrame:
        numeric_df = self._df.select_dtypes(include="number")
        if numeric_df.empty:
            return pd.DataFrame()
        return numeric_df.describe()

if __name__ == "__main__":
    raw = {
        "name": ["Алия", "Нурлан", "Дана", "Асель", "Марат"],
        "age": [20, 21, 19, 22, 20],
        "score": [85, 55, 90, 72, 60],
    }
    ds = TabularDataset(raw)

    print("shape:", ds.shape)
    print("columns:", ds.column_names)
    print("\nhead_info:")
    print(ds.head_info())
    print("\nnumeric_summary:")
    print(ds.numeric_summary())
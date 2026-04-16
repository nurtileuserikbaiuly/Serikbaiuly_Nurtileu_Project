import abc
import pandas as pd

class DataFrameTransform(abc.ABC):

    def _validate(self, df: pd.DataFrame, columns: list[str]) -> None:
        if not isinstance(df, pd.DataFrame):
            raise TypeError("Ожидается pd.DataFrame")
        missing = [c for c in columns if c not in df.columns]
        if missing:
            raise ValueError(f"Отсутствуют столбцы: {missing}")

    @abc.abstractmethod
    def apply(self, df: pd.DataFrame) -> pd.DataFrame:
        pass


class FilterByScoreTransform(DataFrameTransform):

    def __init__(self, min_score: float, column: str = "score"):
        self._min_score = min_score
        self._column = column

    def apply(self, df: pd.DataFrame) -> pd.DataFrame:
        self._validate(df, [self._column])
        result = df.copy()
        return result[result[self._column] >= self._min_score].reset_index(drop=True)


class AddPassedColumnTransform(DataFrameTransform):

    def __init__(self, column: str = "score", threshold: float = 70.0):
        self._column = column
        self._threshold = threshold

    def apply(self, df: pd.DataFrame) -> pd.DataFrame:
        self._validate(df, [self._column])
        result = df.copy()
        result["passed"] = result[self._column] >= self._threshold
        return result


if __name__ == "__main__":
    df = pd.DataFrame({
        "name": ["Алия", "Нурлан", "Дана", "Асель", "Марат"],
        "score": [85, 55, 90, 72, 60],
    })

    print("После фильтра (>= 65):")
    print(FilterByScoreTransform(min_score=65).apply(df))

    print("\nС добавленным столбцом passed:")
    print(AddPassedColumnTransform().apply(df))


import abc
import pandas as pd


class MissingValueStrategy(abc.ABC):

    @abc.abstractmethod
    def apply(self, df: pd.DataFrame) -> pd.DataFrame:
        pass


class FillNumericMeanStrategy(MissingValueStrategy):

    def __init__(self, columns: list[str]):
        self._columns = columns

    def apply(self, df: pd.DataFrame) -> pd.DataFrame:
        result = df.copy()
        for col in self._columns:
            if col not in result.columns:
                raise ValueError(f"Столбец '{col}' не найден")
            if not pd.api.types.is_numeric_dtype(result[col]):
                raise ValueError(f"Столбец '{col}' не числовой")
            result[col] = result[col].fillna(result[col].mean())
        return result


class DropRowsAnyNaStrategy(MissingValueStrategy):

    def __init__(self, columns: list[str] | None = None):
        # columns=None — проверяем все столбцы
        self._columns = columns

    def apply(self, df: pd.DataFrame) -> pd.DataFrame:
        result = df.copy()
        if self._columns:
            return result.dropna(subset=self._columns).reset_index(drop=True)
        return result.dropna().reset_index(drop=True)


class MissingValueProcessor:

    def __init__(self, strategy: MissingValueStrategy):
        self._strategy = strategy

    def process(self, df: pd.DataFrame) -> pd.DataFrame:
        return self._strategy.apply(df)



if __name__ == "__main__":
    df = pd.DataFrame({
        "name": ["Алия", "Нурлан", "Дана", "Асель", "Марат"],
        "score": [85.0, None, 90.0, None, 60.0],
    })

    print("До обработки:", df.shape)
    print(df)

    filled = MissingValueProcessor(FillNumericMeanStrategy(["score"])).process(df)
    print("\nПосле заполнения средним:", filled.shape)
    print(filled)

    dropped = MissingValueProcessor(DropRowsAnyNaStrategy()).process(df)
    print("\nПосле удаления строк с NaN:", dropped.shape)
    print(dropped)
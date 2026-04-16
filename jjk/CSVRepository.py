import pathlib
import pandas as pd
from TabularDataset import TabularDataset


class CsvRepository:

    def __init__(self, path: str | pathlib.Path, required_columns: list[str]):
        self._path = pathlib.Path(path)
        self._required_columns = required_columns

    def load(self) -> TabularDataset:
        df = pd.read_csv(self._path)
        missing = [c for c in self._required_columns if c not in df.columns]
        if missing:
            raise ValueError(f"В файле отсутствуют столбцы: {missing}")
        return TabularDataset(df)

    def save(self, dataset: TabularDataset) -> None:
        dataset.data.to_csv(self._path, index=False)


if __name__ == "__main__":
    csv_path = pathlib.Path("students.csv")

    # создаём тестовый файл
    pd.DataFrame({
        "name": ["Алия", "Нурлан", "Дана"],
        "age": [20, 21, 19],
        "score": [85, 55, 90],
    }).to_csv(csv_path, index=False)

    repo = CsvRepository(csv_path, required_columns=["name", "age", "score"])
    ds = repo.load()
    print("Загружено, shape:", ds.shape)
    print(ds.head_info())

    modified = ds.data
    modified["score"] = modified["score"] + 5
    repo.save(TabularDataset(modified))
    print("\nСохранено с +5 к баллам.")
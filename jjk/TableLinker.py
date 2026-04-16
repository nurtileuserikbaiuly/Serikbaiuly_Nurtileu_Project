import pandas as pd


class TableLinker:

    @staticmethod
    def merge_left(left: pd.DataFrame, right: pd.DataFrame, on: str) -> pd.DataFrame:
        return pd.merge(left.copy(), right.copy(), on=on, how="left")

    @staticmethod
    def concat_rows(parts: list[pd.DataFrame]) -> pd.DataFrame:
        return pd.concat([p.copy() for p in parts], ignore_index=True)

if __name__ == "__main__":
    left = pd.DataFrame({
        "id": [1, 2, 3, 4],
        "name": ["Алия", "Нурлан", "Дана", "Асель"],
    })
    right = pd.DataFrame({
        "id": [1, 2, 5],
        "grade": ["A", "C", "B"],
    })

    print("merge_left:")
    print(TableLinker.merge_left(left, right, on="id"))

    part1 = pd.DataFrame({"name": ["Алия"], "score": [85]})
    part2 = pd.DataFrame({"name": ["Нурлан"], "score": [55]})

    print("\nconcat_rows:")
    print(TableLinker.concat_rows([part1, part2]))

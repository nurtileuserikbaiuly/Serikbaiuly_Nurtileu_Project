import pandas as pd
from DataFrameTransform import DataFrameTransform, FilterByScoreTransform, AddPassedColumnTransform


class PandasTransformPipeline:

    
    def __init__(self, *transforms: DataFrameTransform):
        self._transforms = list(transforms)

    def run(self, df: pd.DataFrame) -> pd.DataFrame:
        result = df.copy()
        for t in self._transforms:
            result = t.apply(result)
        return result

    def describe(self) -> str:
        names = [type(t).__name__ for t in self._transforms]
        return " -> ".join(names)


if __name__ == "__main__":
    df = pd.DataFrame({
        "name": ["Алия", "Нурлан", "Дана", "Асель", "Марат", "Бекзат", "Жанна"],
        "score": [85, 55, 90, 72, 60, 78, 45],
    })

    pipeline = PandasTransformPipeline(
        FilterByScoreTransform(min_score=60),
        AddPassedColumnTransform()
    )

    print("Pipeline:", pipeline.describe())
    print(pipeline.run(df))
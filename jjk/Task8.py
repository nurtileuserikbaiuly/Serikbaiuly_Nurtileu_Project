import pathlib
import pandas as pd

from TabularDataset import TabularDataset
from CSVRepository import CsvRepository
from DataFrameTransform import FilterByScoreTransform, AddPassedColumnTransform
from PandasTransformPipeline import PandasTransformPipeline
from GroupScoreReport import GroupScoreReport
from TableLinker import TableLinker
from MissingValueStrategy import (
    MissingValueProcessor,
    FillNumericMeanStrategy,
    DropRowsAnyNaStrategy,
)


def demo_task1():
    print("=" * 50)
    print("ЗАДАНИЕ 1 — TabularDataset")
    print("=" * 50)
    ds = TabularDataset({
        "name": ["Алия", "Нурлан", "Дана", "Асель", "Марат"],
        "age": [20, 21, 19, 22, 20],
        "score": [85, 55, 90, 72, 60],
    })
    print("shape:", ds.shape)
    print("columns:", ds.column_names)
    print(ds.head_info())
    print(ds.numeric_summary())


def demo_task2():
    print("\n" + "=" * 50)
    print("ЗАДАНИЕ 2 — CsvRepository")
    print("=" * 50)
    csv_path = pathlib.Path("students.csv")
    pd.DataFrame({
        "name": ["Алия", "Нурлан", "Дана"],
        "age": [20, 21, 19],
        "score": [85, 55, 90],
    }).to_csv(csv_path, index=False)

    repo = CsvRepository(csv_path, required_columns=["name", "age", "score"])
    ds = repo.load()
    print("Загружено, shape:", ds.shape)

    modified = ds.data
    modified["score"] = modified["score"] + 5
    repo.save(TabularDataset(modified))
    print("Сохранено с +5 к баллам.")


def demo_task3():
    print("\n" + "=" * 50)
    print("ЗАДАНИЕ 3 — Преобразования")
    print("=" * 50)
    df = pd.DataFrame({
        "name": ["Алия", "Нурлан", "Дана", "Асель", "Марат"],
        "score": [85, 55, 90, 72, 60],
    })
    print("После фильтра (>= 65):")
    print(FilterByScoreTransform(min_score=65).apply(df))
    print("\nС добавленным столбцом passed:")
    print(AddPassedColumnTransform().apply(df))


def demo_task4():
    print("\n" + "=" * 50)
    print("ЗАДАНИЕ 4 — Pipeline")
    print("=" * 50)
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


def demo_task5():
    print("\n" + "=" * 50)
    print("ЗАДАНИЕ 5 — GroupScoreReport")
    print("=" * 50)
    df = pd.DataFrame({
        "student": ["Алия", "Алия", "Нурлан", "Нурлан", "Дана", "Дана", "Асель", "Асель"],
        "subject": ["Матан", "Физика", "Матан", "Физика", "Матан", "Физика", "Матан", "Физика"],
        "score": [85, 90, 55, 60, 70, 75, 80, 65],
    })
    report = GroupScoreReport(df)
    print("Агрегация по студентам:")
    print(report.aggregate_by_student())
    print("\nСводная таблица:")
    print(report.pivot_subjects())


def demo_task6():
    print("\n" + "=" * 50)
    print("ЗАДАНИЕ 6 — TableLinker")
    print("=" * 50)
    left = pd.DataFrame({"id": [1, 2, 3, 4], "name": ["Алия", "Нурлан", "Дана", "Асель"]})
    right = pd.DataFrame({"id": [1, 2, 5], "grade": ["A", "C", "B"]})
    print("merge_left:")
    print(TableLinker.merge_left(left, right, on="id"))
    part1 = pd.DataFrame({"name": ["Алия"], "score": [85]})
    part2 = pd.DataFrame({"name": ["Нурлан"], "score": [55]})
    print("\nconcat_rows:")
    print(TableLinker.concat_rows([part1, part2]))


def demo_task7():
    print("\n" + "=" * 50)
    print("ЗАДАНИЕ 7 — MissingValueStrategy")
    print("=" * 50)
    df = pd.DataFrame({
        "name": ["Алия", "Нурлан", "Дана", "Асель", "Марат"],
        "score": [85.0, None, 90.0, None, 60.0],
    })
    print("До обработки:", df.shape)
    filled = MissingValueProcessor(FillNumericMeanStrategy(["score"])).process(df)
    print("После заполнения средним:", filled.shape)
    print(filled)
    dropped = MissingValueProcessor(DropRowsAnyNaStrategy()).process(df)
    print("После удаления строк с NaN:", dropped.shape)
    print(dropped)


def demo_final():
    print("\n" + "=" * 50)
    print("ИТОГОВАЯ СБОРКА")
    print("=" * 50)
    students_df = pd.DataFrame({
        "student": ["Алия", "Нурлан", "Дана", "Асель", "Марат", "Бекзат", "Жанна"],
        "subject": ["Матан"] * 7,
        "score": [85, 55, 90, 72, 60, 78, 45],
    })

    pipeline = PandasTransformPipeline(
        FilterByScoreTransform(min_score=60),
        AddPassedColumnTransform()
    )
    processed = pipeline.run(students_df)
    print("После pipeline:")
    print(processed)

    report = GroupScoreReport(processed)
    print("\nОтчёт по студентам:")
    print(report.aggregate_by_student())

    groups_df = pd.DataFrame({
        "student": ["Алия", "Нурлан", "Дана", "Асель", "Марат", "Бекзат", "Жанна"],
        "group": ["ИС-21", "ИС-21", "ИС-22", "ИС-22", "ИС-21", "ИС-22", "ИС-21"],
    })
    final = TableLinker.merge_left(processed, groups_df, on="student")
    print("\nИтоговая таблица:")
    print(final)


if __name__ == "__main__":
    print("ФИО: Иванов Иван Иванович  |  Группа: ИС-21\n")
    demo_task1()
    demo_task2()
    demo_task3()
    demo_task4()
    demo_task5()
    demo_task6()
    demo_task7()
    demo_final()
import pandas as pd


class GroupScoreReport:

    def __init__(self, df: pd.DataFrame,
                 student_col: str = "student",
                 subject_col: str = "subject",
                 score_col: str = "score"):
        self._df = df.copy()
        self._student = student_col
        self._subject = subject_col
        self._score = score_col

    def aggregate_by_student(self) -> pd.DataFrame:
        return (
            self._df
            .groupby(self._student)[self._score]
            .agg(count="count", mean="mean", min="min", max="max")
            .reset_index()
        )

    def pivot_subjects(self) -> pd.DataFrame:
        return self._df.pivot_table(
            index=self._student,
            columns=self._subject,
            values=self._score,
            aggfunc="mean"
        )

if __name__ == "__main__":
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
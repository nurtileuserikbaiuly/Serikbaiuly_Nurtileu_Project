import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
from PlotConfig import PlotConfig
from SeabornPlotFactory import SeabornPlotFactory
from CsvDataRepository import CsvDataRepository
from Plots import LinePlot


class VisualizationReportService:
    def __init__(self, repository: CsvDataRepository, factory: SeabornPlotFactory, output_dir: Path):
        self.repository = repository
        self.factory = factory
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def build_student_report(self, df: pd.DataFrame) -> dict:
        paths = {}

        numeric_cols = df.select_dtypes(include="number").columns.tolist()
        x_col = df.columns[0]
        y_col = numeric_cols[0]

        line_config = PlotConfig((8, 5), "Line: Dynamics", x_col, y_col)
        line_plot = LinePlot(df[x_col].tolist(), df[y_col].tolist(), line_config, self.output_dir)
        paths["line"] = line_plot.save("report_line.png")

        means = df[numeric_cols].mean().reset_index()
        means.columns = ["feature", "mean_value"]
        bar_config = PlotConfig((8, 5), "Bar: Mean Values", "feature", "mean_value")
        fig_bar = self.factory.barplot(means, x="feature", y="mean_value", config=bar_config)
        bar_path = self.output_dir / "report_bar.png"
        fig_bar.savefig(bar_path)
        plt.close(fig_bar)
        paths["bar"] = bar_path

        corr = df[numeric_cols].corr()
        heat_config = PlotConfig((8, 6), "Heatmap: Correlations", "", "")
        fig_heat = self.factory.heatmap(corr, config=heat_config)
        heat_path = self.output_dir / "report_heatmap.png"
        fig_heat.savefig(heat_path)
        plt.close(fig_heat)
        paths["heatmap"] = heat_path

        return paths


if __name__ == "__main__":
    df = pd.DataFrame({
        "month": [1, 2, 3, 4, 5],
        "sales": [100, 150, 120, 200, 180],
        "expenses": [80, 90, 85, 100, 95]
    })

    repo = CsvDataRepository()
    factory = SeabornPlotFactory()
    service = VisualizationReportService(repo, factory, Path("output"))

    result = service.build_student_report(df)
    for key, path in result.items():
        print(f"{key}: {path}")
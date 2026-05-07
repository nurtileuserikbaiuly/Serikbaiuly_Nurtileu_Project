from pathlib import Path
from BasePlot import BasePlot
from PlotConfig import PlotConfig
from Plots import LinePlot, BarPlot, HistogramPlot


class PlotPipeline:
    def __init__(self, plots: list):
        self.plots = plots

    def run_all(self) -> list:
        paths = []
        for i, plot in enumerate(self.plots):
            filename = f"{plot.__class__.__name__}_{i}.png"
            path = plot.save(filename)
            paths.append(path)
        return paths

    def describe(self) -> list:
        return [plot.__class__.__name__ for plot in self.plots]


if __name__ == "__main__":
    out = Path("output")

    line_config = PlotConfig((8, 5), "Line Chart", "X", "Y")
    bar_config = PlotConfig((8, 5), "Bar Chart", "Category", "Value")
    hist_config = PlotConfig((8, 5), "Histogram", "Value", "Frequency")

    plots = [
        LinePlot([1, 2, 3, 4], [10, 20, 15, 30], line_config, out),
        BarPlot(["A", "B", "C"], [5, 10, 7], bar_config, out),
        HistogramPlot([1, 2, 2, 3, 3, 3, 4], bins=4, config=hist_config, output_dir=out),
    ]

    pipeline = PlotPipeline(plots)

    print("Plots in pipeline:", pipeline.describe())

    saved_paths = pipeline.run_all()
    for path in saved_paths:
        print(f"Saved: {path}")
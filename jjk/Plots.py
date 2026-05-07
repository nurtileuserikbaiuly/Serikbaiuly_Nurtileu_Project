import matplotlib.pyplot as plt
from pathlib import Path
from PlotConfig import PlotConfig
from BasePlot import BasePlot


class LinePlot(BasePlot):
    def __init__(self, x, y, config: PlotConfig, output_dir: Path):
        super().__init__(config, output_dir)
        self.x = x
        self.y = y

    def draw(self) -> plt.Figure:
        if self.config.style:
            plt.style.use(self.config.style)
        fig, ax = plt.subplots(figsize=self.config.figsize)
        ax.plot(self.x, self.y)
        self.config.apply(ax)
        return fig


class BarPlot(BasePlot):
    def __init__(self, categories, values, config: PlotConfig, output_dir: Path):
        super().__init__(config, output_dir)
        self.categories = categories
        self.values = values

    def draw(self) -> plt.Figure:
        if self.config.style:
            plt.style.use(self.config.style)
        fig, ax = plt.subplots(figsize=self.config.figsize)
        ax.bar(self.categories, self.values)
        self.config.apply(ax)
        return fig


class HistogramPlot(BasePlot):
    def __init__(self, data, bins, config: PlotConfig, output_dir: Path):
        super().__init__(config, output_dir)
        self.data = data
        self.bins = bins

    def draw(self) -> plt.Figure:
        if self.config.style:
            plt.style.use(self.config.style)
        fig, ax = plt.subplots(figsize=self.config.figsize)
        ax.hist(self.data, bins=self.bins)
        self.config.apply(ax)
        return fig


if __name__ == "__main__":
    out = Path("output")

    line_config = PlotConfig((8, 5), "Line Chart", "Month", "Sales")
    line = LinePlot([1, 2, 3, 4], [10, 20, 15, 30], line_config, out)
    path = line.save("line.png")
    print(f"Saved: {path}")

    bar_config = PlotConfig((8, 5), "Bar Chart", "Category", "Value")
    bar = BarPlot(["A", "B", "C"], [5, 10, 7], bar_config, out)
    path = bar.save("bar.png")
    print(f"Saved: {path}")

    hist_config = PlotConfig((8, 5), "Histogram", "Value", "Frequency")
    hist = HistogramPlot([1, 2, 2, 3, 3, 3, 4, 4, 5], bins=5, config=hist_config, output_dir=out)
    path = hist.save("histogram.png")
    print(f"Saved: {path}")

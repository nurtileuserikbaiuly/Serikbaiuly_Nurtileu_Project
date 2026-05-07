import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from PlotConfig import PlotConfig


class SeabornPlotFactory:
    def barplot(self, df: pd.DataFrame, x: str, y: str, config: PlotConfig) -> plt.Figure:
        if df.empty:
            raise ValueError
        if x not in df.columns:
            raise ValueError
        if y not in df.columns:
            raise ValueError

        fig, ax = plt.subplots(figsize=config.figsize)
        sns.barplot(data=df, x=x, y=y, ax=ax)
        config.apply(ax)
        return fig

    def heatmap(self, df: pd.DataFrame, config: PlotConfig, annot: bool = True) -> plt.Figure:
        if df.empty:
            raise ValueError

        fig, ax = plt.subplots(figsize=config.figsize)
        sns.heatmap(df, annot=annot, ax=ax)
        config.apply(ax)
        return fig


if __name__ == "__main__":
    factory = SeabornPlotFactory()

    df = pd.DataFrame({
        "category": ["A", "B", "C"],
        "value": [10, 20, 15]
    })

    config = PlotConfig((8, 5), "Seaborn Bar", "category", "value")
    fig = factory.barplot(df, x="category", y="value", config=config)
    plt.show()
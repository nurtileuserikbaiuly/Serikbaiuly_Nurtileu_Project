import abc
import matplotlib.pyplot as plt
from pathlib import Path
from PlotConfig import PlotConfig


class BasePlot(abc.ABC):
    def __init__(self, config: PlotConfig, output_dir: Path):
        self.config = config
        self.output_dir = output_dir

    @abc.abstractmethod
    def draw(self) -> plt.Figure:
        pass

    def save(self, filename: str) -> Path:
        fig = self.draw()
        self.output_dir.mkdir(parents=True, exist_ok=True)
        path = self.output_dir / filename
        fig.savefig(path)
        plt.close(fig)
        return path
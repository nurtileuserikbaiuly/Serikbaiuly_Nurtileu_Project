import matplotlib.pyplot as plt


class PlotConfig:
    def __init__(self, figsize, title, x_label, y_label, style=None):
        self.figsize = figsize
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        self.style = style

    def apply(self, ax):
        ax.set_title(self.title)
        ax.set_xlabel(self.x_label)
        ax.set_ylabel(self.y_label)
        ax.grid(True)


if __name__ == "__main__":
    config = PlotConfig(
        figsize=(8, 5),
        title="Plot Config",
        x_label="X",
        y_label="Y",
    )

    if config.style:
        plt.style.use(config.style)

    fig, ax = plt.subplots(figsize=config.figsize)
    ax.plot([1, 2, 3], [4, 5, 6])
    config.apply(ax)
    plt.show()
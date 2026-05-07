import matplotlib.pyplot as plt
from week09 import DataLoader, CenterSelector
from week10 import KMeans
from week11 import ClusterDataFrame


class ScatterPlotter:

    def __init__(self, df, centers):
        self.df = df
        self.centers = centers

    def plot(self, filename="scatter.png"):
        colors = {0: "red", 1: "blue", 2: "green"}

        plt.figure(figsize=(7, 5))

        for cluster_id, group in self.df.groupby("cluster_id"):
            plt.scatter(
                group["x"],
                group["y"],
                c=colors[cluster_id],
                label=f"Кластер {cluster_id}",
                alpha=0.6,
                s=50
            )

        plt.scatter(
            self.centers[:, 0],
            self.centers[:, 1],
            c="black",
            marker="X",
            s=300,
            label="Центры",
            zorder=5
        )

        plt.title("Кластеры (k=3)")
        plt.legend()
        plt.tight_layout()
        plt.savefig(filename)
        print(f"График сохранён: {filename}")


if __name__ == "__main__":
    loader = DataLoader("points.csv")
    points = loader.load()

    selector = CenterSelector(points, k=3, seed=42)
    centers = selector.random_k()

    kmeans = KMeans(points, centers)
    labels, final_centers = kmeans.fit(n_iter=10)

    cdf = ClusterDataFrame(points, labels)
    df = cdf.build()

    plotter = ScatterPlotter(df, final_centers)
    plotter.plot("scatter.png")
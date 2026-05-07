import numpy as np
import matplotlib.pyplot as plt


from week09 import DataLoader, CenterSelector


class KMeans:

    def __init__(self, points, centers):
        self.points = points
        self.centers = centers
        self.labels = None

    def _assign(self):
        distances = np.linalg.norm(
            self.points[:, np.newaxis] - self.centers, axis=2
        )
        self.labels = np.argmin(distances, axis=1)

    def _update_centers(self):
        new_centers = np.zeros_like(self.centers)
        for k in range(len(self.centers)):
            cluster_points = self.points[self.labels == k]
            if len(cluster_points) > 0:
                new_centers[k] = cluster_points.mean(axis=0)
            else:
                new_centers[k] = self.centers[k]
        self.centers = new_centers

    def fit(self, n_iter=10):
        for i in range(n_iter):
            self._assign()
            self._update_centers()
            print(f"Итерация {i+1}: орталықтар =\n{self.centers}")
        return self.labels, self.centers


class KMeansPlotter:

    def __init__(self, points, labels, centers):
        self.points = points
        self.labels = labels
        self.centers = centers

    def plot(self, filename="result.png"):
        colors = ["red", "blue", "green"]
        plt.figure(figsize=(7, 5))
        for k in range(len(self.centers)):
            mask = self.labels == k
            plt.scatter(
                self.points[mask, 0], self.points[mask, 1],
                c=colors[k], label=f"Кластер {k}", alpha=0.6
            )
        plt.scatter(
            self.centers[:, 0], self.centers[:, 1],
            c="black", marker="X", s=200, label="Орталықтар"
        )
        plt.title("K-means (k=3, 10 итерация саны)")
        plt.legend()
        plt.tight_layout()
        plt.savefig(filename)
        plt.show()
        print(f"График сохранён: {filename}")


if __name__ == "__main__":
    loader = DataLoader("points.csv")
    points = loader.load()

    selector = CenterSelector(points, k=3, seed=42)
    centers = selector.random_k()

    kmeans = KMeans(points, centers)
    labels, final_centers = kmeans.fit(n_iter=10)

    plotter = KMeansPlotter(points, labels, final_centers)
    plotter.plot("result.png")

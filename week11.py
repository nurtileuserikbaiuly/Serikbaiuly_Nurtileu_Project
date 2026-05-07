import pandas as pd
from week09 import DataLoader, CenterSelector
from week10 import KMeans


class ClusterDataFrame:

    def __init__(self, points, labels):
        self.points = points
        self.labels = labels
        self.df = None

    def build(self):
        self.df = pd.DataFrame({
            "x": self.points[:, 0],
            "y": self.points[:, 1],
            "cluster_id": self.labels
        })
        print(self.df)
        print(f"\nБарлық жол: {len(self.df)}")
        return self.df

if __name__ == "__main__":

    loader = DataLoader("points.csv")
    points = loader.load()

    selector = CenterSelector(points, k=3, seed=42)
    centers = selector.random_k()

    kmeans = KMeans(points, centers)
    labels, final_centers = kmeans.fit(n_iter=10)

    cdf = ClusterDataFrame(points, labels)
    df = cdf.build()

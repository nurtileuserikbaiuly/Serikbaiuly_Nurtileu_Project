import pandas as pd
from week09 import DataLoader, CenterSelector
from week10 import KMeans


class CentersTable:

    def __init__(self, centers):
        self.centers = centers   # массив k x 2
        self.df = None

    def build(self):
        self.df = pd.DataFrame({
            "cluster_id": range(len(self.centers)),
            "x": self.centers[:, 0],
            "y": self.centers[:, 1]
        })
        print(self.df)
        return self.df

    def save(self, filepath="centers.csv"):
        self.df.to_csv(filepath, index=False)
        print(f"\nСохранено в файл: {filepath}")

if __name__ == "__main__":
    loader = DataLoader("points.csv")
    points = loader.load()

    selector = CenterSelector(points, k=3, seed=42)
    centers = selector.random_k()

    kmeans = KMeans(points, centers)
    labels, final_centers = kmeans.fit(n_iter=10)

    ct = CentersTable(final_centers)
    ct.build()
    ct.save("centers.csv")
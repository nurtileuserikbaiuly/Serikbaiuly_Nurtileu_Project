import numpy as np


class DataLoader:

    def __init__(self, filepath):
        self.filepath = filepath
        self.points = None

    def load(self):
        self.points = np.loadtxt(self.filepath, delimiter=",", skiprows=1)
        print(f"Загружено точек: {len(self.points)}")
        return self.points


class CenterSelector:

    def __init__(self, points, k=3, seed=42):
        self.points = points
        self.k = k
        self.seed = seed

    def first_k(self):
        centers = self.points[:self.k].copy()
        print(f"Стартовые центры (первые {self.k}):\n{centers}")
        return centers

    def random_k(self):
        rng = np.random.default_rng(self.seed)
        idx = rng.choice(len(self.points), size=self.k, replace=False)
        centers = self.points[idx].copy()
        print(f"Стартовые центры (случайные, seed={self.seed}):\n{centers}")
        return centers


if __name__ == "__main__":
    loader = DataLoader("points.csv")
    points = loader.load()

    selector = CenterSelector(points, k=3, seed=42)
    centers = selector.random_k()

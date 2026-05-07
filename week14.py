from flask import Flask, request, jsonify
from week09 import DataLoader, CenterSelector
from week10 import KMeans

app = Flask(__name__)


class KMeansAPI:

    def __init__(self, k=3, seed=42, n_iter=10):
        self.k = k
        self.seed = seed
        self.n_iter = n_iter

    def run(self, points_list):
        import numpy as np


        points = np.array(points_list)


        selector = CenterSelector(points, k=self.k, seed=self.seed)
        centers = selector.random_k()


        kmeans = KMeans(points, centers)
        labels, final_centers = kmeans.fit(n_iter=self.n_iter)


        return {
            "labels": labels.tolist(),
            "centers": final_centers.tolist()
        }


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    points_list = data["points"]

    api = KMeansAPI(k=3, seed=42, n_iter=10)
    result = api.run(points_list)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)

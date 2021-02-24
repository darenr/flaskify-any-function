from typing import List, Set, Dict, Tuple, Optional

from sklearn import datasets
from sklearn.svm import SVC
import logging
logging.basicConfig(level=logging.DEBUG)


def train_model():
    logging.info(f" * Iris::train_model")
    iris = datasets.load_iris()
    clf = SVC()
    clf.fit(iris.data, iris.target_names[iris.target])

    return clf


clf = train_model()


# 5.8, 2.7, 5.1, 1.9 -> versicolor
def score(sepal_length: float, sepal_width: float, petal_length: float, petal_width: float) -> str:
    logging.info(f" * Iris::score")
    return list(clf.predict([[sepal_length, sepal_width, petal_length, petal_width]]))

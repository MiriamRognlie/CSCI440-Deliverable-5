from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

def ridge_regression(x, y, p):
    model = make_pipeline(PolynomialFeatures(p), Ridge())
    model.fit(x, y)
    return model.predict(x)
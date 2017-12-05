import scipy.stats
from sklearn import linear_model
from sklearn.metrics import mean_squared_error

def linear_regression(x, y):
    regr = linear_model.LinearRegression()  # calculate regression line for this data
    regr.fit(x, y)
    pred = regr.predict(x)
    # The coefficients
    print('Regression Coefficient (Slope): \n',
          regr.coef_)  # prints out the regression line coefficients from the scatter plot
    print('Pearson\'s Correlation: ', scipy.stats.pearsonr(x,
                                                           y))  # calculates and prints Pearson's correlation coefficient
    #  based on data from the scatter plot
    print('Spearman\'s Correlation: ', scipy.stats.spearmanr(x,
                                                             y))  # calculates and prints Spearman's rank correlation
    # coefficient based on data from the scatter plot
    print("Mean squared error: %.2f" % mean_squared_error(x, y))  # calculates and prints the mean squared error

    return pred
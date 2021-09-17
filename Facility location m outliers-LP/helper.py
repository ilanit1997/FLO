import matplotlib.pyplot as plt
from sklearn import datasets
import pandas as pd
import numpy as np
import random


def plot_points(paid_facilities, clients, outliers, cost, m, z, P, type='LP'):
    x_clients, y_clients = [P[0][c] for c in clients], [P[1][c] for c in clients]
    scatter_clients = plt.scatter(x_clients, y_clients, color='black')
    x_outliers, y_outliers = [P[0][c] for c in outliers], [P[1][c] for c in outliers]
    scatter_outliers = plt.scatter(x_outliers, y_outliers, color='red')
    x_facilities, y_facilities = [P[0][c] for c in paid_facilities], [P[1][c] for c in paid_facilities]
    scatter_facilities = plt.scatter(x_facilities, y_facilities, color='green')
    plt.legend((scatter_clients, scatter_outliers, scatter_facilities),
               ('clients', 'outliers', 'paid facilities'),
               loc='upper left',
               fontsize=8)
    title = 'FLO with {}, with m={} z= {}, COST: {}'.format(type, m,z, cost)
    plt.title(title)
    plt.show()

def generate_date(type = 'Boston'):
    try:
        if type == 'Boston':
            boston = datasets.load_boston()
            boston_df = pd.DataFrame(boston.data)
            columns = boston.feature_names
            boston_df.columns = columns
            x, y = boston_df['INDUS'], boston_df['TAX']
            P = np.array([np.array([x1, y1]) for x1, y1 in zip(x, y)])
            P = P[np.unique(P[:, 1], return_index=True)[1]].T
            P = P[:, :]

            # P = P[:, np.random.permutation(P.shape[1])]
        elif type == 'Simple':
            P = np.array([[1,1], [1,1.5], [0.5, 1], [1.4,1.5], [5,5], [2,2], [3,3]]).T

        return P

    except ValueError:
        print('Invalid data set type')
        raise




def cost_func(clients, facilities, distance, z = -1):
    total_cost = 0 if z == -1 else z*len(facilities)
    for c in clients:
        if len(distance[c, facilities])>0:
            total_cost+= min(distance[c,facilities])
    return total_cost

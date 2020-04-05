import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import zscore


def series_example():
    temp = [
        3, 4, 3, 2, 5, 6, 5, 4, 5, 6,
        7, 8, 7, 6, 5, 6, 7, 8, 9, 8,
        7, 6, 7, 6, 5, 6, 5, 4, 5, 4,
        3
    ]
    date = [i+1 for i in range(len(temp))]
    ts = pd.Series(temp, date)
    print('\n', ts[:10])
    input()

    stat = ts.describe()
    print('\n', stat)
    input()

    plt.figure()
    ts.plot()
    plt.grid(True)
    plt.show()


def get_test_df():
    par_names = ['sex', 'pay', 'age']
    values = [
        ['m', 45362, 46],
        ['f', 34252, 35],
        ['m', 34252, 36],
        ['f', 59789, 50],
        ['f', 23145, 25],
        ['f', 96748, 46],
        ['m', 95647, 55],
        ['m', 34235, 30],
        ['m', 42518, 35],
    ]
    data = pd.DataFrame(values, columns=par_names)
    return data


def frame_example():
    data = get_test_df()
    print(data)

    stat = data.describe()
    input()
    print(stat)

    input()
    print('\n', data.groupby('sex').mean())


def plotting_example():
    data = get_test_df()

    # plt.figure()
    data.plot.scatter(x='pay', y='age')
    plt.show()

    males = data.loc[data['sex'] == 'm']
    females = data.loc[data['sex'] == 'f']

    # plt.figure()
    ax = males.plot.scatter(x='pay', y='age', label='Males', color='b')
    females.plot.scatter(x='pay', y='age', label='Females', color='r', ax=ax)
    plt.show()


def z_scores_example():
    data = get_test_df()
    print(data)
    z_data = data[['pay', 'age']].apply(zscore)
    print(z_data)
    plt.figure()
    z_data.plot.scatter(x='pay', y='age')
    plt.show()


if __name__ == "__main__":
    # series_example()
    # frame_example()
    plotting_example()
    # z_scores_example()

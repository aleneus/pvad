from pandas import read_csv
import matplotlib.pyplot as plt


def load_csv_example():
    file_name = "data/data-1.csv"
    data = read_csv(
        file_name,
        sep=',',
        header=0,
        index_col=0,
    )
    print(data)
    input()
    print('\n', data['Outcome'])
    input()
    stat = data.describe()
    print('\n', stat)
    input()
    print('\n', stat['Outcome'])

    # fig = plt.figure()
    data.plot.line()
    plt.show()
    # plt.close(fig)

    profit = data['Income'] - data['Outcome']
    # fig = plt.figure()
    profit.plot.line()
    plt.show()
    # plt.close()


if __name__ == "__main__":
    load_csv_example()

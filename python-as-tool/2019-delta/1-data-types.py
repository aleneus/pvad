import numpy as np


def variable():
    a = 1
    a = a + 2
    print(a)

    a = "hello, "
    a = a + "world!"
    print(a)


def list_basic():
    lst = [1, 2, 3, 4, 5]

    print(lst)
    print(len(lst))
    print(lst[0])
    print(lst[-1])
    print(lst[len(lst)//2])

    print(lst[1:3])
    print(lst[:3])
    print(lst[2:])

    print(lst[::2])
    print(lst[1::2])

    lst.append(6)
    print(lst)


def list_iter():
    lst = [i*2 for i in range(10)]
    print(lst)
    for v in lst:
        print(v, end=' ')
    print()


def tuple_example():
    tpl = (1, 2, 3)
    print(tpl[0])
    try:
        tpl.append(4)
    except Exception as expt:
        print(expt)


def dict_example():
    human = {
        'name': "Aleksander",
        'age': 34,
        'address': {
            'town': "Arkhangelsk",
            'street': "Karla Marksa",
            'house': "76",
        },
        'phones': [
            "87687687",
            "86546565",
            "85454545",
        ],
    }

    print(human['name'])
    print(human['phones'][0])
    print(human['address']['street'])

    print()
    human['hobbey'] = "Reading"
    for key in human:
        print(key)


def array_example():
    a = np.array([0]*10)
    print(a)
    print()
    for i in range(len(a)):
        print(a[i], end=' ')
    print()
    m = np.zeros(shape=(3, 10))
    print(m)
    print(m[1, 2])


def process_list():
    a = [1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 8, 8, 6, 7, 7, 6, 6]
    n = 0
    for x_p, x_c in zip(a[:-1], a[1:]):
        if x_p == x_c:
            n += 1
    print(n)


def main():
    pass
    variable()
    list_basic()
    list_iter()
    tuple_example()
    dict_example()
    array_example()
    process_list()


if __name__ == "__main__":
    main()

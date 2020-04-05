"""Model for access to datasets."""
import json
import quants


Q_SCHEME = {
    'p': {
        'reqs': ['vm', 'va', 'im', 'ia'],
        'func': quants.active_power_n
    },
    'q': {
        'reqs': ['vm', 'va', 'im', 'ia'],
        'func': quants.reactive_power_n
    },
    's': {
        'reqs': ['p', 'q'],
        'func': quants.full_power_n
    }
}


class DatasetModel:
    """Model for getting pmu dicts from dataset in JSON file."""
    def __init__(self, file_name, q_scheme=Q_SCHEME):
        with open(file_name) as buf:
            dataset = json.load(buf)
        self.times = dataset['times']
        self.data = dataset['data']
        self.q_scheme = q_scheme

    def __add_quant(self, pmu, key):
        if key in self.data[pmu]:
            return

        if key not in self.q_scheme:
            return

        for req in self.q_scheme[key]['reqs']:
            self.__add_quant(pmu, req)

        for req in self.q_scheme[key]['reqs']:
            if req not in self.data[pmu]:
                return

        func = self.q_scheme[key]['func']
        args = []
        for req in self.q_scheme[key]['reqs']:
            args.append(self.data[pmu][req])
        self.data[pmu][key] = func(*args)

    def get_quant(self, key):
        """Return pmu dict with quant. Example: get_quant('f')."""
        res = {'times': self.times}
        for pmu in self.data:
            self.__add_quant(pmu, key)
            if key in self.data[pmu]:
                res[pmu] = self.data[pmu][key]
        return res


def repr_data(data):
    print("times: {}".format(data['times']))
    for key in sorted(list(data.keys())):
        if key == "times":
            continue
        print("{}: {}".format(key, data[key]))


if __name__ == "__main__":
    model = DatasetModel("data/dataset.json")
    repr_data(model.get_quant('s'))
    repr_data(model.get_quant('s'))
    repr_data(model.get_quant('p'))

import sqlite3


class Sample:
    def __init__(self):
        self.data = None


class Group:
    def __init__(self):
        self.name = None
        self.samples = []


class Model:
    def __init__(self):
        self.conn = None

    def open_db(self, fname):
        self.conn = sqlite3.connect(fname)

    def samples(self, group_id=None):
        if self.conn is None:
            return
        c = self.conn.cursor()
        query = """
        SELECT s.data
        FROM sample as s, data_group as g, sample_group as sg
        WHERE s.id = sg.sample_id AND g.id = sg.group_id
        """
        if group_id is None:
            data = c.execute(query)
        if group_id is not None:
            query += " AND g.id=?"
            data = c.execute(query, (group_id))
        samples = []
        for row in c:
            sample = Sample()
            sample.data = row[0]
            samples.append(sample)
        return samples

    def many_another_methods(self):
        pass


class Controller:
    def __init__(self):
        self.model = None
        self.view = None

    def set_model(self, model):
        self.model = model

    def set_view(self, view):
        self.view = view

    def open_db(self, fname):
        self.model.open_db(fname)

    def samples(self, group_id=None):
        samples = self.model.samples(group_id)
        self.view.show_samples(samples)


class View:
    def show_samples(self, samples):
        for sample in samples:
            print(sample.data)


def main():
    m = Model()
    c = Controller()
    v = View()
    c.set_model(m)
    c.set_view(v)

    c.open_db("data/data-2.sqlite.db")
    c.samples(group_id="1")
    print()
    c.samples(group_id="2")
    print()
    c.samples()


if __name__ == "__main__":
    main()

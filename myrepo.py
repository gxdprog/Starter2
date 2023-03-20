from create_db import Session


class MyRepository:

    def __init__(self):
        self.session = Session()

    def get_something(self, something):
        return self.session.query(something)

    def add_something(self, something):
        self.session.add(something)
        self.session.commit()

    def del_something(self, something):
        self.session.delete(something)
        self.session.commit()

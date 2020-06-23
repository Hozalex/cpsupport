from app.model.rest import Rest
from app.model.parser import Parser


class Main:
    def __init__(self):
        self.rest = Rest()
        self.parser = Parser()


if __name__ == "__main__":
    m = Main()
    m.parser.file_extract()


    # print(m.rest.get())
    # m.rest.post()
    print(m.parser.company.name, m.parser.company.observer_ids, m.parser.company.phone)

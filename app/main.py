from app.model.rest import Rest
from app.model.parser import Parser
from app.model.json_factory import JsonFactory


class Main:
    def __init__(self):
        self.rest = Rest()
        self.parser = Parser()
        self.jsonFactory = JsonFactory()


if __name__ == "__main__":
    m = Main()
    json = m.parser.file_extract()
    print(m.parser.d)

    # print(m.rest.get())
    # m.rest.post()
    # m.jsonFactory.get_json(m.parser.company)

from app.model.Company import Company
from docx import Document
import json


class Main:
    def __init__(self):
        self.company = Company('')

    def file_extract(self):
        try:
            doc = Document('C:/Users/kav1302/PycharmProjects/cpsupport/test.DOCX')
            for p in doc.paragraphs:
                text = p.text
                local_string = text.split(': ')

                if local_string[:1] == ['Название']:
                    self.company.name = local_string[1:]
                elif local_string[:1] == ['Сайт']:
                    self.company.site = local_string[1:]
                elif local_string[:1] == ['email']:
                    self.company.email = local_string[1:]
                elif local_string[:1] == ['телефон']:
                    self.company.phone = local_string[1:]
                elif local_string[:1] == ['адрес']:
                    self.company.address = local_string[1:]
                elif local_string[:1] == ['комментарий']:
                    self.company.comment = local_string[1:]
                elif local_string[:1] == ['ответственный сотрудник']:
                    self.company.observer_ids = local_string[1:]

        except Exception as ex:
            write_log(ex)


def write_log(exception):
    print(exception)


if __name__ == "__main__":
    m = Main()
    m.file_extract()

    print(str(m.company.name), '\n', m.company.observer_ids, '\n', m.company.phone)

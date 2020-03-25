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
                    self.company.name = ''.join(local_string[1:])
                elif local_string[:1] == ['Сайт']:
                    self.company.site = ''.join(local_string[1:])
                elif local_string[:1] == ['email']:
                    self.company.email = ''.join(local_string[1:])
                elif local_string[:1] == ['телефон']:
                    self.company.phone = ''.join(local_string[1:])
                elif local_string[:1] == ['адрес']:
                    self.company.address = ''.join(local_string[1:])
                elif local_string[:1] == ['комментарий']:
                    self.company.comment = ''.join(local_string[1:])
                elif local_string[:1] == ['ответственный сотрудник']:
                    self.company.observer_ids = ''.join(local_string[1:])

        except Exception as ex:
            write_log(ex)


def write_log(exception):
    print(exception)


if __name__ == "__main__":
    m = Main()
    m.file_extract()

    print(m.company.name, m.company.observer_ids, m.company.phone)

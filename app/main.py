from app.model.company import Company
from app.model.rest import Rest
from docx import Document
import json
from _datetime import datetime


class Main:
    def __init__(self):
        self.company = Company('')
        self.rest = Rest()

    def file_extract(self):
        try:
            doc = Document('test.docx')
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


def write_log(*args):
    with open('log.txt', 'a') as log_file:
        date = datetime.strftime(datetime.now(), '%d.%m.%Y %H:%M:%S')
        error = str(f'{date} {args}')
        log_file.write(error + '\n')


if __name__ == "__main__":
    m = Main()
    m.file_extract()
    print(m.rest.get())
    print(m.company.name, m.company.observer_ids, m.company.phone)

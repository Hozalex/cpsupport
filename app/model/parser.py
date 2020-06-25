from docx import Document
from _datetime import datetime
import json


class Parser:
    def __init__(self):
        self.d = {'name': '', 'site': '', 'email': '', 'phone': '', 'address': '', 'comment': '', 'observer_ids': ''}

    def file_extract(self):
        try:
            doc = Document('test.docx')
            for p in doc.paragraphs:
                text = p.text
                local_string = text.split(': ')

                if local_string[:1] == ['Название']:
                    self.d['name'] = ''.join(local_string[1:])
                elif local_string[:1] == ['Сайт']:
                    self.d['site'] = ''.join(local_string[1:])
                elif local_string[:1] == ['email']:
                    self.d['email'] = ''.join(local_string[1:])
                elif local_string[:1] == ['телефон']:
                    self.d['phone'] = ''.join(local_string[1:])
                elif local_string[:1] == ['адрес']:
                    self.d['address'] = ''.join(local_string[1:])
                elif local_string[:1] == ['комментарий']:
                    self.d['comment'] = ''.join(local_string[1:])
                elif local_string[:1] == ['ответственный сотрудник']:
                    self.d['observer_ids'] = ''.join(local_string[1:])

        except Exception as ex:
            write_log(ex)

        return json.dumps(self.d, ensure_ascii=False)


def write_log(*args):
    with open('log.txt', 'a') as log_file:
        date = datetime.strftime(datetime.now(), '%d.%m.%Y %H:%M:%S')
        error = str(f'{date} {args}')
        log_file.write(error + '\n')

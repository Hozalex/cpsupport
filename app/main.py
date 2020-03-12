from app.model.Company import Company
from docx import Document
import re
import json


def file_extract():
    doc = Document('C:/Users/kav1302/PycharmProjects/cpsupport/test.DOCX')
    email = None
    for p in doc.paragraphs:
        text = p.text
        print(text)
        email = re.search(r'[a-z0-9.\-+_]+@[a-z0-9.\-+_]+\.[a-z]+', text)


def main():
    file_extract()


main()

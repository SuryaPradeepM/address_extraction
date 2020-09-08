import PyPDF2
import os
from pprint import pprint


pages = []
path = os.path.join(os.getcwd(), 'docs')

for pdf in os.listdir('docs'):
    print(pdf)
    print(os.path.join(path, pdf))
    pdfFileObj = open(os.path.join(path, pdf), 'rb')
    print(pdfFileObj)
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pages += [pdfReader.getPage(p).extractText() for p in range(pdfReader.numPages)]
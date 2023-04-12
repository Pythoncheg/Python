import csv
import View
def writeFile(values):
    with open('notepad.csv', mode="a", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ";", lineterminator="\n")
        file_writer.writerow([values[0], values[1],values[2]])

def readFile():
    with open('notepad.csv', encoding='utf-8') as r_file:
        file_reader = csv.DictReader(r_file, delimiter = ";")
        fileList = [ i for i in file_reader]
        return fileList


def writeEmptyFile():
    with open('notepad.csv', mode="w", encoding='utf-8') as w:
        file_writer = csv.writer(w, delimiter = ";", lineterminator="\n")
        file_writer.writerow(['Заголовок','Содержание','Дата создания'])

def writeFileAfterDel(values):
    with open('notepad.csv', mode="w", encoding='utf-8') as w_file:
        newFile = True
        file_writer = csv.writer(w_file, delimiter = ";", lineterminator="\n")
        if newFile==True:
            file_writer.writerow(['Заголовок','Содержание','Дата создания'])
            newFile = False
        file_writer.writerow([values[0], values[1],values[2]])
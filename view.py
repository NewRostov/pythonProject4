import uuid
from datetime import datetime


def inputCommand():
    print(f'---------------------------------------------\n'
          f'\t < Приложение заметки > \n'
          f'Выберите действие:\n'
          f'0 > создать файл приложения (Внимание!!! исли файл существует -> будет перезаписан!) \n'
          f'1 > создать заметку \n'
          f'2 > вывести все заметки \n'
          f'3 > сортировка заметок \n'
          f'4 > вывести информацию по отдельным полям заметок \n'
          f'5 > поиск заметки \n'
          f'6 > полная корректировка заметки\n'
          f'7 > редактирование заголовка заметки \n'
          f'8 > удалить заметку\n'
          f'9 > экспорт/импорт данных из/в файл \n'
          f'10 > выход из программы\n')
    choice = input()
    print()
    return choice


def inputNote():                  # 1> добавить заметку
    id = str(uuid.uuid1())[0:5]
    header = checkEmptyString(input('Введите заголовок заметки: ').lower())
    body = checkEmptyString(input('Введите тело заметки: ').lower())
    date = datetime.now()
    data = (f'id: {id}; ЗАГОЛОВОК: {header}; ТЕЛО ЗАМЕТКИ: {body}; дата/время: {date};\n')
    # print(data)
    return data


def checkEmptyString(string):  # проверка для вводимых данных
    while len(string) < 1:
        print('введена пустая строка!')
        string = input('Введите заново:')
    else:
        return string


def sortNote():                 # 3 > сортировка заметок
    value_sorting = input(f'введите: \n'
                          f'0 > сортировка по id \n'
                          f'1 > сортировка по заголовку \n'
                          f'2 > сортировка по содержанию \n'
                          f'3 > сортировка по дате/времени создания \n')
    return value_sorting


def choicePrintFieldNote():    # 4 > вывести все заметки по отдельному полю
    while True:
        value_print = input(f'введите: \n'
                            f'0 > вывести по id \n'
                            f'1 > вывести по заголовку \n'
                            f'2 > вывести по содержанию \n'
                            f'3 > вывести по дате/времени создания \n')
        return value_print


def searchNote():              # 5 > поиск заметки
    str_search = input('введите для поиска ОДНО из значений:\n'
                       f' <id>, \n'
                       f' или  <заголовок>, \n'
                       f' или  <слово из содержания заметки>, \n'
                       f' или  <дату/время создания (format 2023-08-09 00:51:47 или раздельно 2023-08-09 или 00:51:47)> : \n')
    return str_search


def rewriteNote():              # 6 > перезапись заметки
    value_change = input(f'полная перезапись >>> режим поиска заметки: \n'
                             f'0 > по id \n'
                             f'1 > по заголовку \n'
                             f'2 > по заголовку \n')
    print('------------------')
    return value_change


def deleteNote():                # 8 > удалить заметку
    value_del = input(f'удаление >>> режим поиска заметки: \n'
                          f'0 > по id \n'
                          f'1 > по заголовку \n'
                          f'2 > по содержимому \n')
    print('------------------')
    return value_del


def expImportFileNotes():  # 9> импорт/экспорт  из/в файл
    value_expImp = input(f'выбор: \n'
                             f'0 > экспорт файла (в формате json) \n'
                             f'1 > импорт файла в формате json \n')
    return value_expImp


if __name__ == '__main__':  # проверка работы функций 
    # inputCommand()
    inputNote()
    # searchNote()
    # sortNote()
    #
    # rewriteNote()
    # correctionNotePartial()
    # deleteNote()
    # expImportFileNotes()
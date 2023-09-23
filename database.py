def add_bd(data):  # 1 > добавить заметку
    with open('note.csv', 'a', encoding='utf-8') as f:
        f.writelines(data)
    print('данные успешно внесены')


def print_bd():  # 2 > вывод списка заметок
    with open('note.csv', 'r', encoding='utf-8') as f:
        print(f.read())


def sort_bd(value_sorting):  # 3 > сортировка заметок
    try:
        if 0 <= int(value_sorting) <= 3:
            with open('note.csv', 'r', encoding='utf-8') as f:
                data = f.readlines()
                data.sort(key=lambda x: x.split(';')[int(value_sorting)])
                with open('note.csv', 'w', encoding='utf-8') as f:
                    f.writelines(data)
            print('---------сортировка выполнена успешно-------------')
            print_bd()
        else:
            print('>>> неправильное значение!')
    except ValueError:
        print('>>> введена строка!')


def printName_bd(value_print):  # 4 > вывести заголовки заметок
    try:
        if 0 <= int(value_print) <= 3:
            with open('note.csv', 'r', encoding='utf-8') as f:
                result = f.readlines()
                for i in result:
                    print(i.split(';')[int(value_print)])
        else:
            print('>>> неправильное значение!')
    except ValueError:
        print('>>> введена строка!')


def search_bd(scan):      # 5 > поиск заметки
    with open('note.csv', 'r', encoding='utf-8') as f:
        data = f.readlines()
        flag = False
        for i in data:
            if scan in i:
                print(i)
                flag = True
        if flag == False:
            print('>>> заметка не найдена!')


import view


def rewriteNode_bd(val):  # 6 > корректировка заметки полная
    try:
        if 0 <= int(val) <= 2:
            with open('note.csv', 'r', encoding='utf-8') as f:
                result = f.readlines()
                for i, v in enumerate(result):
                    print(i, v.split(';')[int(val)])
                print('------------------')
                value_change = int(input('Введите цифру соответствующую выбранной заметке для внесения изменений: '))
                new_data = view.inputNote()
                # print(new_data)
                for i, v in enumerate(result):
                    if i == value_change:
                        result[i] = new_data
                    #     print(result[i])
                    # print(i, v.split()[val])
                print('информация обновлена')
                with open('note.csv', 'w', encoding='utf-8') as f:
                    f.writelines(result)
        else:
            print('>>> неправильное значение!')
    except ValueError:
        print('>>> введена строка!')


def correctionNote_bd():  # 7 > корректировка заголовка заметки
    with open('note.csv', 'r', encoding='utf-8') as f:
        result = f.readlines()
        value_user = str(input('Введите заголовок существующей заметки для ее изменения: '))
        for i, v in enumerate(result):
            if value_user in v.split(';')[1]:
                print(i, value_user)
        value_user_change = int(input('Введите номер изменяемой позиции: '))
        val_new = str(input('Введите новые данные: '))
        for i, v in enumerate(result):
            if i == value_user_change:
                # print(result[i].split(';')[value])
                result[i] = result[i].replace((result[i].split(';')[1]), " ЗАГОЛОВОК: " + val_new, 1)
                print('->', result[i])
        print('информация обновлена')
        with open('note.csv', 'w', encoding='utf-8') as f:
            f.writelines(result)


def deleteNote_bd(name):  # 8 > удалить заметку
    try:
        if 0 <= int(name) <= 2:
            with open('note.csv', 'r', encoding='utf-8') as f:
                result = f.readlines()
                for i, v in enumerate(result):
                    print(i, v.split(';')[int(name)])
                print('------------------')
                value_del = int(input('Введите цифру соответствующую удаляемой заметке: '))
                for i, v in enumerate(result):
                    if i == value_del:
                        del result[i]
                print('заметка успешно удалена')
                with open('note.csv', 'w', encoding='utf-8') as f:
                    f.writelines(result)
        else:
            print('>>> неправильное значение!')
    except ValueError:
        print('>>> введена строка!')


import json


def expImport_bd(value_expImp):  # 9 > экспорт файла (в формате json)
    try:
        if int(value_expImp) == 0:
            with open('note.csv', 'r', encoding='utf-8') as f:
                data = f.readlines()
            with open('json_note.json', 'w', encoding='utf-8') as f:
                json_note = json.dump(data, f)
                print('Объект записан в формате json')
                f.close()
        elif int(value_expImp) == 1:  # 9 > импорт файла в формате json
            with open('json_note.json', 'r', encoding='utf-8') as f:
                result = json.load(f)
                # print(result)
            with open('note.csv', 'a', encoding='utf-8') as f:
                f.writelines(result)
            print('данные из файла импортированы в приложение')
            f.close()
        else:
            print('>>> неправильное значение!')
    except ValueError:
        print('>>> введена строка!')


import datetime

def saveLog_bd(message):  # логирование работы прогр.
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    # print(result)
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


if __name__ == '__main__':
    # sort_bd(2)
    # printName_bd()
    # rewriteNode_bd(1)
    # correctionNote_bd()
    # deleteNote_bd(2)
    expImport_bd(1)
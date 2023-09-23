import view, database
from database import saveLog_bd


def main():
    saveLog_bd('старт')
    while True:
        ask = view.inputCommand()
        if ask == '0':
            open('note.csv', 'w')
            print('выполнено!')
        elif ask == '1':
            data = view.inputNote()
            database.add_bd(data)
        elif ask == '2':
            database.print_bd()
        elif ask == '3':
            value_sorting = view.sortNote()
            database.sort_bd(value_sorting)
        elif ask == '4':
            value_print = view.choicePrintFieldNote()
            database.printName_bd(value_print)
        elif ask == '5':
            scan = view.searchNote()
            database.search_bd(scan)
        elif ask == '6':
            value_change = view.rewriteNote()
            database.rewriteNode_bd(value_change)
        elif ask == '7':
            database.correctionNote_bd()
        elif ask == '8':
            value_del = view.deleteNote()
            database.deleteNote_bd(value_del)
        elif ask == '9':
            value_expImp = view.expImportFileNotes()
            database.expImport_bd(value_expImp)
        elif ask == '10':
            print('выполнен выход из программы!')
            print('---------The end---------')
            saveLog_bd('конец')
            break
        else:
            print('введите корректное значение!')
            view.inputCommand()
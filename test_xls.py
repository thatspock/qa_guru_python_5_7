import xlrd
import os.path


# TODO оформить в тест, добавить ассерты и использовать универсальный путь

def test_xls():
    download_folder = 'resources'
    xls_file_path = os.path.join(download_folder, 'file_example_XLS_10.xls')

    assert os.path.exists(xls_file_path), f'XLS file {xls_file_path} was not found'

    book = xlrd.open_workbook(xls_file_path)

    assert book.nsheets == 1
    assert book.sheet_names() == ['Sheet1']

    print(f'\nКоличество листов {book.nsheets}')
    print(f'Имена листов {book.sheet_names()}')

    sheet = book.sheet_by_index(0)

    assert sheet.ncols == 8
    assert sheet.nrows == 10
    assert sheet.cell_value(rowx=0, colx=1) == 'First Name'

    print(f'Количество столбцов {sheet.ncols}')
    print(f'Количество строк {sheet.nrows}')
    print(f'Пересечение строки 9 и столбца 1 = {sheet.cell_value(rowx=0, colx=1)}')
    # печать всех строк по очереди
    for rx in range(sheet.nrows):
        print(sheet.row(rx))

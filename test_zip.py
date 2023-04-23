from zipfile import ZipFile
import os.path


def test_zip():
    download_folder = 'resources'
    zip_file_path = os.path.join(download_folder, 'final.zip')

    pdf_pytest = os.path.join(download_folder, 'docs-pytest-org-en-latest.pdf')
    file_xls = os.path.join(download_folder, 'file_example_XLS_10.xls')
    file_xlsx = os.path.join(download_folder, 'file_example_XLSX_50.xlsx')
    logo = os.path.join(download_folder, 'selenium_logo.png')

    list_files = [pdf_pytest, file_xls, file_xlsx, logo]

    with ZipFile(zip_file_path, 'w') as zipF:
        for file in list_files:
            zipF.write(file)

    with ZipFile(zip_file_path) as zipR:
        for file in list_files:
            unzipped_path = zipR.namelist()[list_files.index(file)]
            assert unzipped_path == file
            assert os.path.getsize(unzipped_path) == os.path.getsize(file)

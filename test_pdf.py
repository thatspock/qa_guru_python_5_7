from pypdf import PdfReader
import os.path


# TODO оформить в тест, добавить ассерты и использовать универсальный путь
def test_pdf():
    download_folder = 'resources'
    pdf_file_path = os.path.join(download_folder, 'docs-pytest-org-en-latest.pdf')

    assert os.path.exists(pdf_file_path), f'Pdf file {pdf_file_path} was not found'

    reader = PdfReader(pdf_file_path)

    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()

    assert number_of_pages == 412
    assert page is not None, 'Page is empty'
    assert text is not None and len(text.strip()) > 0, 'Text is empty'

    print(f'\n1: {number_of_pages}')
    print(f'2: {page}')
    print(f'3: {text}')

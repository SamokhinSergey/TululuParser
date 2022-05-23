import requests
import os
from bs4 import BeautifulSoup
from pathvalidate import sanitize_filename


def download_txt(url, filename, folder='books/'):
    """Функция для скачивания текстовых файлов.
    Args:
        url (str): Cсылка на текст, который хочется скачать.
        filename (str): Имя файла, с которым сохранять.
        folder (str): Папка, куда сохранять.
    Returns:
        str: Путь до файла, куда сохранён текст.
    """
    filename = sanitize_filename(filename)
    folder = sanitize_filename(folder)
    payload = {"id": book_id}
    response = requests.get(url, payload, allow_redirects=False)
    check_for_redirect(response)
    response.raise_for_status()
    file_patch = os.path.join(folder, filename + '.txt')
    with open(file_patch, 'wb') as file:
        file.write(response.content)
    return file_patch


def check_books_dir():
    books_dir = "books"
    if not os.path.exists(books_dir):
        os.makedirs(books_dir)
    return books_dir


def check_for_redirect(tululu_response):
    if tululu_response.is_redirect:
        raise requests.HTTPError


def book_name(book_id):
    url = f"https://tululu.org/b{book_id}"
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'lxml')
    title_tag = soup.find(class_='ow_px_td').find('h1')
    book_name = title_tag.text.split(':')[0].strip()
    book_autror = title_tag.text.split(':')[2].strip()
    print(book_name, book_autror)
    return book_name


for book_id in range(10):

    try:
        url = "https://tululu.org/txt.php"
        download_txt(url, book_name(book_id), check_books_dir())

    except requests.HTTPError:
        print(f"Книги с id {book_id} не существует на сайте")

    except:
        print("1")

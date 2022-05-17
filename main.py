import requests
import os


def check_books_dir():
    books_dir = "books"
    if not os.path.exists(books_dir):
        os.makedirs(books_dir)
    return books_dir


for id in range(10):
    url = f"https://tululu.org/txt.php?id={id}"
    response = requests.get(url)
    response.raise_for_status()
    filename = f'{check_books_dir()}/id{id}.txt'
    with open(filename, 'wb') as file:
        file.write(response.content)

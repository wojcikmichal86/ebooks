import requests
from bs4 import BeautifulSoup
from time import time


def ebookpoint(books):
    current_time = time()
    file = requests.get('http://ebookpoint.pl/plugins/new/xml/external/imbiria_ebook_ebookpoint.xml')
    #file.encoding = "utf-8"
    plain_text = file.text
    soup = BeautifulSoup(plain_text, "html.parser")
    book = soup.find("o")
    print(book)
    while book.find_next_sibling('o') is not None:
        name = book.find('name')
        if name.contents[0] not in books.keys():
            books[name.contents[0]] = {'ebookpoint': book['price']}
        else:
            books[name.contents[0]].update({'ebookpoint': book['price']})
        book2 = book.find_next_sibling('o')
        print(book2)
        book = book2
    print(time() - current_time)
    print('Current number of books: '+str(len(books)))
    return books

if __name__ == "__main__":
    ebookpoint({})
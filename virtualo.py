import requests
from bs4 import BeautifulSoup
from time import time



def virtualo(books):
    current_time = time()
    file = requests.get('https://virtualo.pl/data/ceneo_ebooks.xml')
    file.encoding = "utf-8"
    plain_text = file.text
    soup = BeautifulSoup(plain_text, "lxml-xml")
    print('soup loaded')
    book = soup.find("o")
    print('o tag located')
    i = 1
    while book.find_next_sibling('o') is not None:
        print('book number {} found'.format(i))
        name = book.find('name')
        if name.contents[0] not in books.keys():
            books[name.contents[0]] = {'virtualo': book['price']}
        else:
            books[name.contents[0]].update({'virtualo': book['price']})
        book2 = book.find_next_sibling('o')
        book = book2
        i+=1
    print(time() - current_time)
    print('Current number of books: '+str(len(books)))

    return books

if __name__ == "__main__":
    virtualo({})




import requests
from bs4 import BeautifulSoup
from time import time


def ebookpoint(books):
    current_time = time()
    file = requests.get('http://ebookpoint.pl/plugins/new/xml/external/imbiria_ebook_ebookpoint.xml')
    #file.encoding = "utf-8"
    plain_text = file.text
    soup = BeautifulSoup(plain_text, "html.parser")
    names = soup.findAll("name")
    prices = soup.findAll("o")
    for i in range(len(names)):
        if names[i].contents[0] not in books.keys():
            books[names[i].contents[0]] = {'ebookpoint': prices[i]['price']}
        else:
            books[names[i].contents[0]].update({'ebookpoint': prices[i]['price']})
    print(time() - current_time)
    print(len(books))
    return books

if __name__ == "__main__":
    ebookpoint({})
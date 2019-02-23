import requests
from bs4 import BeautifulSoup
from time import time


def ebp_audio(books):
    current_time = time()
    file = requests.get('https://ebookpoint.pl/plugins/new/xml/external/imbiria_mp3_ebookpoint.xml')
    #file.encoding = "utf-8"
    plain_text = file.text
    soup = BeautifulSoup(plain_text, "html.parser")
    names = soup.findAll("name")
    prices = soup.findAll("o")
    for i in range(len(names)):
        if names[i].contents[0] not in books.keys():
            books[names[i].contents[0]] = {'ebookpoint audio': prices[i]['price']}
        else:
            books[names[i].contents[0]].update({'ebookpoint audio': prices[i]['price']})
    print(time() - current_time)
    print(len(books))
    return books

if __name__ == "__main__":
    ebp_audio({})
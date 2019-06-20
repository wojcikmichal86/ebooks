import requests
from time import time
from xml.etree import ElementTree
import os

def get_page(filename, url):
    if os.path.isfile(filename):
        with open(filename, 'r') as input_data:
            content = input_data.read()
    else:
        response = requests.get(url)
        content = response.text
        with open(filename, 'w') as output_data:
            output_data.write(content)
    return(content)

def ebookpoint(books):
    current_time = time()
    print('requesting file')
    get_page('ebookpoint.xml', 'http://ebookpoint.pl/plugins/new/xml/external/imbiria_ebook_ebookpoint.xml')

    xml_iter = ElementTree.iterparse('ebookpoint.xml', events=('start', 'end'))
    for event, elem in xml_iter:
        if elem.tag == 'o':
            try:
                name = elem.find('name').text
                if name not in books.keys():
                    books[name] = {'virtualo': elem.attrib['price']}
                else:
                    books[name].update({'virtualo': elem.attrib['price']})
            except:
                pass
        elem.clear()

    print(time() - current_time)
    print('Current number of books: '+str(len(books)))

    return books

if __name__ == "__main__":
    ebookpoint({})

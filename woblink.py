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

def woblink(books):
    current_time = time()
    print('requesting file')
    get_page('woblink.xml', 'http://woblink.com/ads4books.xml')

    xml_iter = ElementTree.iterparse('woblink.xml', events=('start', 'end'))
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
    os.remove('woblink.xml')

    return books

if __name__ == "__main__":
    woblink({})

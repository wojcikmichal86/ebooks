import requests
from time import time
from xml.dom import minidom



def virtualo(books):
    current_time = time()
    print('requesting xml')
    file = requests.get('https://virtualo.pl/data/ceneo_ebooks.xml')
    print('xml requested')
    file.encoding = "utf-8"
    print('encoded')
    data = file.text
    while data.find('<name>') > 0:
        price_start_index = data.find('price=')
        data = data[price_start_index+7:]
        price_end_index = data.find('" ')
        price = data[:price_end_index]
        name_start_index = data.find('<name>')
        name_end_index = data.find('</name>')
        name = data[name_start_index+15:name_end_index-3]
        print(name)
        print(price)
        print(len(books))
        if name not in books.keys():
            books[name] = {'virtualo': price}
        else:
            books[name].update({'virtualo': price})
        data = data[name_end_index+10:]



    '''
    DOMTree = minidom.parseString(file.text)
    print('DOMTree parsed')
    cNodes = DOMTree.childNodes
    nodes = cNodes[0].getElementsByTagName("o")
    for node in nodes:
        price = node.getAttribute("price")
        name = node.getElementsByTagName("name")[0].firstChild.wholeText
        
    print('plain text created')
    soup = BeautifulSoup(plain_text, "lxml-xml")
    print('soup loaded')
    book = soup.find("o")
    print('o tag located')
    i = 1
    while book.find_next_sibling('o') is not None:
        #print('book number {} found'.format(i))
        name = book.find('name')


        book2 = book.find_next_sibling('o')
        book = book2
        i+=1
    '''
    print(time() - current_time)
    print('Current number of books: '+str(len(books)))
    print(books)
    return books

if __name__ == "__main__":
    virtualo({})




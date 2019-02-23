import requests
from bs4 import BeautifulSoup
from time import time


def homepage():
    current_time = time()
    file = requests.get('http://woblink.com/ads4books.xml?fbclid=IwAR2Zumd7pJB_usUe9XvSynH5j1tVhmKVLKZ7qgH2HyJMSe0gt-6Z24vNR6A')
    file.encoding = "utf-8"
    plain_text = file.text
    soup = BeautifulSoup(plain_text, "lxml-xml")
    names = soup.findAll("name")
    tags = soup.findAll("o")
    for i in range(len(names)):
        print(names[i].contents[0])
        print(tags[i]['price'])
    print(time() - current_time)


'''
def ebooks():
        tree = ET.ElementTree(file = requests.get('http://woblink.com/ads4books.xml?fbclid=IwAR2Zumd7pJB_usUe9XvSynH5j1tVhmKVLKZ7qgH2HyJMSe0gt-6Z24vNR6A'))
        root = tree.getroot()
        print(root)


        source_code = requests.get(url)
        
        soup = BeautifulSoup(plain_text, "lxml")
        dni=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

ebooks()
'''

homepage()
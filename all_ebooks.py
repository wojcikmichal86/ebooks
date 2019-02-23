from woblink import woblink
from virtualo import virtualo
from ebp_audio import ebp_audio
from ebookpoint import ebookpoint
import json


def get_all():
	books={}

	woblink(books)
	virtualo(books)
	ebp_audio(books)
	ebookpoint(books)

	big_json = {}
	titles = []
	for book in books.keys():
		titles.append(book)

	for i in range(len(titles)):
		big_json.update({str(i): {'title': titles[i], 'prices': books[titles[i]]}})

	print(big_json)

	with open('all_books.json', 'w') as fp:
	    json.dump(big_json, fp)
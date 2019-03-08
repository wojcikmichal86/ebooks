from woblink import woblink
from virtualo import virtualo
from ebp_audio import ebp_audio
from ebookpoint import ebookpoint
import json
from datetime import datetime



def get_all():
	print("Updating database on: "+str(datetime.now()))
	updated = "Last updated on: "+str(datetime.now())
	books = {}
	#woblink(books)
	#virtualo(books)
	ebp_audio(books)
	#ebookpoint(books)

	big_json = {}
	titles = []
	for book in books.keys():
		titles.append(book)

	for i in range(len(titles)):
		big_json.update({str(i): {'title': titles[i], 'prices': books[titles[i]], 'updated': updated}})

	with open('all_books.json', 'w') as fp:
	    json.dump(big_json, fp)

if __name__ == "__main__":
    get_all()
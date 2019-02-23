from flask import Flask
from flask import jsonify
import json
from all_ebooks import get_all
from werkzeug.routing import BaseConverter

app = Flask(__name__)

class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]

app.url_map.converters['regex'] = RegexConverter

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/<regex("[abcABC0-9]{1,7}"):u>')
def find_book(u):
	all_books = json.load(open("all_books.json"))
	return jsonify(all_books["%s" %(u)])

@app.route("/all")
def all():
	get_all()
	return "Books uploaded"




if __name__ == '__main__':
    app.run(debug=True)
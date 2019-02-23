from flask import Flask
from flask import jsonify
import json
from all_ebooks import get_all

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/1")
def find_book():
	all_books = json.load(open("all_books.json"))
	return jsonify(all_books['1'])

@app.route("/all")
def all():
	get_all()
	return "Books uploaded"




if __name__ == '__main__':
    app.run(debug=True)
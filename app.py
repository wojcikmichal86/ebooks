from flask import Flask
from flask import jsonify
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/7214")
def find_book():
	all_books = json.load(open("all_books.json"))
	return jsonify(all_books['7214'])



if __name__ == '__main__':
    app.run(debug=True)
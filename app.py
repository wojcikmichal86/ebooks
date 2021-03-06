from flask import Flask
from flask import jsonify
import json
from all_ebooks import get_all
from werkzeug.routing import BaseConverter
from apscheduler.scheduler import Scheduler

app = Flask(__name__)

'''
sched = Scheduler() # Scheduler object
sched.add_interval_job(get_all, minutes=10)
sched.start()
'''
	

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

@app.route('/update')
def update():
    get_all()
    return('updating books')


if __name__ == '__main__':
    app.run(debug=False, use_reloader=False)
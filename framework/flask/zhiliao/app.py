from flask import Flask, jsonify
import config

app = Flask(__name__)
app.config.from_object(config)

books = [
    {"id": 1, "name": "sanguo"},
    {"id": 2, "name": "shuihu"},
    {"id": 3, "name": "honglou"},
    {"id": 4, "name": "shuihu"},

]


@app.route('/')
def hello_world():  # put application's code here
    return {"username": "i奥朋友"}


@app.route('/book/<int:book_id>')
def book_detail(book_id):
    for book in books:
        if book_id == book['id']:
            return book
    return f"{book_id}的图书 没有找到"


@app.route('/book/list')
def book_list():
    return jsonify(books)


if __name__ == '__main__':
    app.run()

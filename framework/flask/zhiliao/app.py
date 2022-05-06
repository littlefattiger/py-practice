from flask import Flask, jsonify, render_template
import config

# from https://www.zlkt.net/book/detail/10/273
from apps import user
from apps import book
from apps import course

app = Flask(__name__)
app.config.from_object(config)
app.register_blueprint(book.bp)
app.register_blueprint(course.bp)
app.register_blueprint(user.bp)

books = [
    {"id": 1, "name": "sanguo"},
    {"id": 2, "name": "shuihu"},
    {"id": 3, "name": "honglou"},
    {"id": 4, "name": "shuihu"},

]


@app.route('/')
def hello_world():  # put application's code here
    return {"username": "i奥朋友"}


@app.route('/about')
def about():
    context = {"username":"apple12"}
    return render_template('about.html', **context)


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

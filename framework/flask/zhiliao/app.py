from flask import Flask, jsonify, render_template, request
import config

# from https://www.zlkt.net/book/detail/10/273
from apps import user
from apps import book
from apps import course
from flask_sqlalchemy import SQLAlchemy

from form import LoginForm

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
    context = {"username": "apple12"}
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


# 数据库的配置变量
HOSTNAME = 'hadoop102'
PORT = '3306'
DATABASE = 'db1'
USERNAME = 'root'
PASSWORD = '111111'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/t1')
def hello_t1():
    engine = db.get_engine()
    with engine.connect() as conn:
        result = conn.execute("select 1")
        print(result.fetchone())
    return "test1"

@app.route('/login', methods =['GET','POST'])
def login():
    if request.method=="GET":
        return render_template("login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            return "successful"
        else:
            return "email or password is wrong"

if __name__ == '__main__':
    app.run()

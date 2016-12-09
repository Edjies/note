from flask import Flask
app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'hello, world'


@app.route('/')
def index():
    return 'index page'


with app.test_request_context():
    print(url_for('index'))
if __name__ == '__main__':
    app.run()
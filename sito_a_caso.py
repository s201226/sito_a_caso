from flask import Flask,render_template,redirect,url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def hello_world():
    return redirect(url_for('index'))

@app.route('/index.html')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run() #host='0.0.0.0' for local

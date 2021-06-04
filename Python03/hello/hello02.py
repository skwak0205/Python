# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    return '<h1><a href="/flask">Hello, Flask!!</a></h1>'

@app.route('/flask')
def hello_flask():
    return '<h1>go <a href="/">root</a></h1>'

if __name__ == '__main__':
    app.run()
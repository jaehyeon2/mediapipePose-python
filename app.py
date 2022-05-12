from urllib import request

from flask import Flask, render_template

import logging
logger = logging.getLogger("app")

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/link')
def link():
    return render_template('link.html')

@app.route('/slinky')
def slinky():
    link = request.form.get("link")
    print(link)

    return render_template('pose.html')

if __name__=='__main__':
    app.run(debug=True)
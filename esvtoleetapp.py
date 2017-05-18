from flask import Flask, render_template, request
from esvtoleet import LeetSpeak, ESVSession
import urllib
import sys
import json
import os

app = Flask(__name__)


@app.errorhandler(Exception)
def exception_handler(error):
    return "!!!!"  + repr(error)


@app.route('/', methods=['POST', 'GET'])
def main():

    # Initiate the leetspeak translator classes
    bible = ESVSession('IP')
    leet = LeetSpeak()

    error = ''
    verse_text = ''
    verse_leet = ''

    if request.method == "GET":
        try:
            verse_ref = request.args.get('verse')
            #verse_ref = request.form['verse']
            verse_text = bible.doPassageQuery(verse_ref)
            verse_leet = leet.toLeet(verse_text)
        except:
            error = "didn't work"
    return render_template('index.html', error=error, verse_text=verse_text, verse_leet=verse_leet)


if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)

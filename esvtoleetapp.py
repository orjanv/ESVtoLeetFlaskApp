from flask import Flask, render_template, request
import urllib
import sys
import json
import os

class LeetSpeak():
    def __init__(self):
        self.x = '1337'

    def toLeet(self, text):
        leet = (
            (('are', 'Are'), 'r'),
            (('ate', 'Ate'), '8'),
            (('that', 'That'), 'tht'),
            (('you', 'You'), 'j00'),
            (('o', 'O'), '0'),
            (('i', 'I'), '1'),
            (('e', 'E'), '3'),
            (('s', 'S'), '5'),
            (('a', 'A'), '4'),
            (('t', 'T'), '7'),
            )
        for symbols, replaceStr in leet:
            for symbol in symbols:
                text = text.replace(symbol, replaceStr)
        return text

class ESVSession:
    def __init__(self, key):
        options = ['include-short-copyright=0',
                   'output-format=plain-text',
                   'include-passage-horizontal-lines=0',
                   'include-heading-horizontal-lines=0',
                   'include-headings=0',
                   'include-footnote-links=0',
                   'include-footnotes=0',
                   'include-passage-references=1']
        self.options = '&'.join(options)
        self.baseUrl = 'http://www.esvapi.org/v2/rest/passageQuery?key=%s' % (key)

    def doPassageQuery(self, passage):
        passage = passage.split()
        passage = '+'.join(passage)
        url = self.baseUrl + '&passage=%s&%s' % (passage, self.options)
        page = urllib.urlopen(url)
        return page.read()


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

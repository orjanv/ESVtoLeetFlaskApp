from flask import Flask, render_template, request
import urllib
import sys
import json
import os
import requests

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


class ESVAPIv3:
    def __init__(self):
        options = ['include-footnotes=false',
            'include-short-copyright=false',
            'include-passage-horizontal-lines=false',
            'include-heading-horizontal-lines=false',
            'include-headings=false']
        self.options = '&'.join(options)
        
    def doPassageQuery(self, passage):
        token = "b8c82a38daaea9fd91c7dcd31b2433f0e4d95172"
        self.url = "https://api.esv.org/v3/passage/text/"
        if passage is not None:
            passage = passage.split()
            passage = '+'.join(passage)
        json_url = self.url + '?q=%s&%s' % (passage, self.options)
        data = requests.get(json_url, headers={'User-Agent': 'Mozilla/5.0', 'Authorization': 'Token ' + token})
        return data.json()['passages'][0]
        
        
app = Flask(__name__)

@app.errorhandler(Exception)
def exception_handler(error):
    return "!!!!"  + repr(error)


@app.route('/', methods=['POST', 'GET'])
def main():

    # Initiate the leetspeak translator classes
    bible = ESVAPIv3()
    leet = LeetSpeak()

    error = ""
    verse_text = ""
    verse_leet = ""

    if request.method == "GET":
        try:
            verse_ref = request.args.get('verse')
            verse_text = bible.doPassageQuery(verse_ref)
            verse_leet = leet.toLeet(verse_text)
        except IndexError:
            error = "didn't work"
    return render_template('index.html', error=error, verse_text=verse_text, verse_leet=verse_leet)


if __name__ == "__main__":
    app.run('0.0.0.0', port=5000, threaded=True)

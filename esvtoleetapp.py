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


class ESVAPIv3:
    def __init__(self):
        return None        
        
    def doPassageQuery(self, passage):

        json_url = 'https://api.esv.org/v3/passage/text/'
        token = 'b8c82a38daaea9fd91c7dcd31b2433f0e4d95172'
        params = {'q': passage}
        headers = {'User-Agent': 'Mozilla/5.0', 'Authorization': 'Token ' + token}
        
        data = requests.get(json_url, 
            params={'q': passage}, 
            headers={'User-Agent': 'Mozilla/5.0', 'Authorization': 'Token ' + token})

        print data.json()['passages'][0]
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

#!/usr/bin/env python

import requests
import sys
import json
import urllib2
import urllib

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


if __name__ == '__main__':

    bible = ESVAPIv3()
    leet = LeetSpeak()

    try:
        print leet.toLeet(bible.doPassageQuery(sys.argv[1]))
        exit(1)
    except IndexError:
        text = ''

    print "The ESV Bible passage leetspeak translator."
    print "Enter a passage to translate to leetspeak (ex. Ecc 3:11) or 'quit' to end."

    passage = raw_input('Enter passage: ')
    while passage != 'quit':
        print leet.toLeet(bible.doPassageQuery(passage))
        passage = raw_input('Enter passage: ')


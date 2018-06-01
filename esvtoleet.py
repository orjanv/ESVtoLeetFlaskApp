#!/usr/bin/env python

import urllib
import requests
import sys
import json
import urllib2

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

class ESVAPIv3:
    def __init__(self):
        return None        
        
    def doPassageQuery(self, passage):

        json_url = 'https://api.esv.org/v3/passage/text/'
        token = 'b8c82a38daaea9fd91c7dcd31b2433f0e4d95172'

        data = requests.get(json_url, 
                      params={'q': passage}, 
                      headers={'User-Agent': 'Mozilla/5.0', 'Authorization': 'Token ' + token})
                

        for p in data:
            print p
            return p


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


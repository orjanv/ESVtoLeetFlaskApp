#!/usr/bin/python
from flup.server.fcgi import WSGIServer
from esvtoleetapp import app

if __name__ == '__main__':
  WSGIServer(app, bindAddress = '/tmp/esvtoleet-fcgi.sock').run()

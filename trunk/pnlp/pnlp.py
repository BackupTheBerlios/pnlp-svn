#!/usr/bin/env python

from xml.sax.handler import ContentHandler
import xml.sax
from urllib2 import urlopen
from urlparse import urlparse
from os import environ, mkdir
from os.path import join, isdir
from uuid import uuid4
from subprocess import Popen
from sys import executable

class PNLPHandler(ContentHandler):
    def startElement(self, name, attrs):
        if name == "pnlp":
            self.codebase = attrs["codebase"]
        elif name == "package":
            self.package = attrs["href"]
        elif name == "application-desc":
            self.main_file = attrs["main-file"]

def parse_pnlp(pnlp):
    handler = PNLPHandler()
    xml.sax.parseString(pnlp, handler)

    return handler

def execute_pnlp(url):
    pnlp = urlopen(url).read()
    config = parse_pnlp(pnlp)

    root = join(environ["HOME"], ".pnlp")
    if not isdir(root):
        mkdir(root)

    dirname = join(root, uuid4().hex)
    mkdir(dirname)
    fo = open(join(dirname, config.main_file), "wb")
    o = urlparse(url)
    file_url = "%s://%s:%s/%s/%s" % \
        (o.scheme, o.hostname, o.port, config.codebase, config.main_file)
    data = urlopen(file_url).read()
    fo.write(data)
    fo.close()

    Popen([executable, config.main_file], cwd=dirname)

if __name__ == "__main__":
    from sys import argv

    execute_pnlp(argv[1])

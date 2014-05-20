#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
converter mbox contents from base64 to utf-8
"""

import base64
# import sys
from html import Html

class Base64_converter:

    def __init__(self, body):
        self.body = body

    def convert(self):
        body = self.body
        body = body.replace("\r\n", "")
        uBody = self.toUnicode(body)
        h = Html(uBody)
        return h.parse()

    def toUnicode(self, line):
        try:
            return base64.b64decode(line)
            # return unicode(base64.b64decode(line),'utf-8')
        except:
            return line

if __name__ == "__main__":
    pass

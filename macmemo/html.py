#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# parse mail html

import re

class Html:

    def __init__(self, body=""):
        self.body = body

    def parse(self):
        body = self.body
        result = {}
        b = re.split("<.+?>", body)
        body_list = [x for x in b if x != ""]
        result["title"] = ""
        num = 0
        if len(body_list[0]) < 40:
            result["title"] = body_list[0]
            num = 1
        result["content"] = ""
        for c in body_list[num:]:
            result["content"] += c+"\r\n"
        return result

# execute program from console.
if __name__ == '__main__':
    test = "<html><head></head><body>テストメール<div><br></div><div>テストで書いてみる。</div><div>この文章はテストプログラムのために書いています。</div><div><br></div><div>pythonはエレガントなコードが書ける。</div><div>例えばリスト内包表記</div><div><br></div><div>x = [y for y in yy]などのように</div><div>色々楽しくコーディングが可能</div><div><br></div><div>おすすめの言語です。</div></body></html>"
    h = Html(test)
    r = h.parse()
    print "====title===="
    print r["title"]
    print
    print "====content===="
    print r["content"]
    print

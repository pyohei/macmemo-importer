#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
mbox parser
basically, this is made for mac_memo importer.
so, parsed files export ./macmemo folder

--USAGE--
python2.7 parse.py xxxx.mbox[MBOX FORMAT]

"""

import mailbox
from base64_converter import Base64_converter as B64

class Parser:

    def __init__(self):
        pass

    def main(self):

        mail_data = mailbox.mbox(FILE_NAME)
        for d in mail_data:
            t = d.get_payload()
            b64 = B64(t)
            data = b64.convert()
            data["date"] = d["Date"]
            if data["title"] == "":
                data["title"] = "none_title"
            if "/" in data["title"]:
                a = data["title"].replace("/", "_")
                data["title"] = "2012_%s"%(a)
            self.write(data)
            # for test command
            # break

    def write(self, data):
        output = open("./macMemo/%s"%(data["title"]), "wb")
        # output = open("./%s"%(data["title"]), "wb")
        output.write(data["date"]+"\r\n\r\n")
        output.write(data["content"])
        print "== Create Diary File =="
        print "title: %s"%(data["title"])
        print

if __name__ == "__main__":
    p = Parser()
    import sys
    if len(sys.argv) == 2:
        FILE_NAME = sys.argv[1]
    else:
        print "need file name"
        quit()
    p.main()

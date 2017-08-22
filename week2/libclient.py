"""Pentester lab bootcamp 
week 2 - http client with library
James Dolan
"""

import sys
import httplib

def main():
        if len(sys.argv) != 2:
            print("./libclient.py [host]")
        else:
            host = sys.argv[1]
            con = httplib.HTTPConnection(host)
            con.request("GET", "/index.html")
            r1 = con.getresponse()
            print(r1.status, r1.reason)
            data = r1.read()
            print(data)

if __name__=='__main__':
    main()


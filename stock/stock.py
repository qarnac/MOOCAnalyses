import urllib
import re

def get_price(symbols_list):
    i = 0
    while i < len(symbols_list):
        url = "http://finance.yahoo.com/q?s=" + symbols_list[i] + "&ql=1"
        regex = '<span id="yfs_l84_[^.]*">(.+?)</span>'
        htmlfile = urllib.urlopen(url)
        htmltext = htmlfile.read()
        pattern = re.compile(regex)
        price = re.findall(pattern, htmltext)
        print "The price of", symbols_list[i], "is", price
        i+=1

def open_symbols_file(FILE_PATH):
    open_file = open("symbols.txt")
    symbols_file = open_file.read()
    symbols_list = symbols_file.split("\n")
    get_price(symbols_list)

if __name__ == "__main__":
    open_symbols_file("symbols.txt")
    

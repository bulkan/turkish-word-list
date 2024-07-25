#!/usr/bin/python

import re
import urllib.request
import urllib.parse

alphabet = "ABCÇDEFGHIİJKLMNOÖPRSŞTUÜVYZ"


def readPage(letter):
    url = "https://tr.wiktionary.org/wiki/" + urllib.parse.quote(
        "Vikisözlük:Sözcük_listesi_({letter})".format(letter=letter)
    )

    with urllib.request.urlopen(url) as response:
        content = response.read()

        words = re.findall(r"<li><a[^>]*>([^<]+)</a>", content.decode("utf-8"), flags=0)
        words.pop()
        print("{} words for {}".format(len(words), letter))
        return words


def getWordList():
    words = []
    for letter in alphabet:
        words += readPage(letter)
    return words


def writeToFile(filename):
    words = getWordList()
    print(len(words))
    f = open(filename, "w")
    f.write("\n".join(words))
    f.close()


writeToFile("words.txt")

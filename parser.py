from urllib.request import urlopen
from pyquery import PyQuery as pq
import operator

CUR_DEPTH = 0
NODES = {}
ROOT_LINK = "http://127.0.0.1:8000"


class Node:
    def __init__(self):
        self.depth = CUR_DEPTH
        self.next = []
        self.printed = False

    def add_next(self, url):
        self.next.append(url)


def parse(url):
    global CUR_DEPTH
    node = Node()
    NODES[url] = node
    try:
        r = urlopen(url)
        content = r.read()
        d = pq(content)
        links = d("a")
        for link in links:
            if link.attrib['href'][0] == '/':
                next_url = ROOT_LINK+link.attrib['href']
            elif 'http' not in link.attrib['href']:
                next_url = url + link.attrib['href']
            else:
                next_url = url
            if link.attrib['href'] == '/':
                next_url = ROOT_LINK
            NODES[url].add_next(next_url)
            if next_url not in NODES.keys():
                CUR_DEPTH += 1
                parse(next_url)
                CUR_DEPTH -= 1
    except Exception:
        print("{} is broken".format(url))


def printNode(link):
    print("{}{}".format("-" * NODES[link].depth, link))
    NODES[link].printed = True
    for url in NODES[link].next:
        if NODES[url].printed == False:
            printNode(url)


if __name__ == "__main__":
    parse(ROOT_LINK)
    printNode(ROOT_LINK)
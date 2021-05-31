#!/usr/bin/env python 3

import sys
from urllib.request import urlopen

def fetch_words(url):
    """
    Ftech a list of word from a URL.
    :param
        url: The url of a UTF-8 text document
    :return:
        A list of strings  containing the words from
        the document.
    """
    with urlopen(url) as story:
        story_words = [];
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)

    return story_words

def print_items(items):
    """ print items one per line .
    :param items: An iterable series  of printable items.
    :return:
    """
    for item in items:
        print(item)

def main(url):
    """ print each word from a text  documentfrom a URL.

    :param url:TheURL of a UTF-8text document.
    :return:
    """
    words = fetch_words(url)
    print_items(words)

if __name__ =='__main__':
    main(sys.argv[1]) # The 0th ard is the module file name
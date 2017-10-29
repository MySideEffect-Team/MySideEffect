#!/usr/bin/python3
# -*- coding: iso-8859-15 -*-
"""
Download new datasets once they are available.
"""
import sys
from bs4 import BeautifulSoup
import urllib.request
from urllib.error import HTTPError
from collections import namedtuple

resp = urllib.request.urlopen("https://open.fda.gov/downloads/")
soup = BeautifulSoup(resp)


Link = namedtuple("Link", ["year", "q"])

def get_link():
    with open("./latest_data_cache.txt", "r") as f:
        year, q = map(int, f.read().split(","))
    newest_known = Link(year=year, q=q)

    year, q = newest_known.year, newest_known.q

    if q == 4:
        q = 1
        year += 1
        part = 1
    else:
        q += 1

    links = ["https://download.open.fda.gov/drug/event/{year}q{q}/drug-event-{part}-of-0023.json.zip".format(year=year, q=q, part=str(i).zfill(4)) for i in range(1, 24)]
    import re
    filenames = [
        re.search("/([^/]+.json.zip)", link).group(1)
        for link in links
    ]
    import urllib.request
    import shutil
    print(filenames[0])
    try:
        with urllib.request.urlopen(links[0]) as response, open(filenames[0], 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
    except HTTPError:
        print("No new data!")
        sys.exit(1)
    else:
        with open("./latest_data_cache.txt", "w") as f:
            f.write("{},{}".format(year, q))


def main():
    get_link()

if __name__ == "__main__":
    main()

#!/usr/bin/python3
# -*- coding: iso-8859-15 -*-
from Bio import Entrez
import argparse

from biopython_wrapper.wrapper import (
    publication_ids, publication_info
)



def main():
    parser = argparse.ArgumentParser(description="Call biopython apis with your email.")
    parser.add_argument(
        "--email", dest="email", default=None
    )

    parser.add_argument(
        "--retmax", dest="retmax", help="Return at most `retmax` records.",
        default="1"
    )

    parser.add_argument(
        "--db", dest="db", help="NCBI Database to query.", default="pubmed"
    )

    parser.add_argument("search_term", help="Search term to query.")

    args = parser.parse_args()

    email = args.email

    if email is None:
        with open("./.email_cache.txt", "r") as f:
            email = f.read().strip()
    else:
        with open("./.email_cache.txt", "w") as f:
            f.write(email)



    ids = publication_ids(
        search_term=args.search_term, retmax=args.retmax, db=args.db
    )

    results = publication_info(publication_ids=ids, db=args.db)

    # TODO: Do something more useful than just print it!
    print(results)

if __name__ == "__main__":
    main()

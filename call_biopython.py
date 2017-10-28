#!/usr/bin/python3
# -*- coding: iso-8859-15 -*-
from Bio import Entrez
import argparse


def main():
    parser = argparse.ArgumentParser(description="Call biopython apis with your email.")
    parser.add_argument(
        "--email", dest="email", default=None
    )

    args = parser.parse_args()

    email = args.email

    if email is None:
        with open("./.email_cache.txt", "r") as f:
            email = f.read().strip()
    else:
        with open("./.email_cache.txt", "w") as f:
            f.write(email)

    Entrez.email = email
    handle = Entrez.elink(db="pubmed", id="26998445", cmd="neighbor_score", rettype="xml")

    records = Entrez.read(handle)

    print(records)


if __name__ == "__main__":
    main()

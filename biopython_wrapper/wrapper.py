from Bio import Entrez

Entrez.email = "freidankm@googlemail.com"


def publication_ids(search_term, db="pubmed", retmax="1", usehistory="y"):

    handle = Entrez.esearch(
        db=db, term=search_term, retmax=retmax, usehistory=usehistory
    )

    records = Entrez.read(handle)

    return records["IdList"]


def publication_info(publication_ids, db="pubmed"):
    handle = Entrez.efetch(
        db=db, id=",".join(publication_ids)
    )

    return handle.read().strip()

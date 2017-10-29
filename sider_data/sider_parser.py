""" Module for reading the sider-files and incorporating them in our Database.
"""
import gzip


def read_tsv(filename):
    """ Reading a zipped file in the tsv format and returning it
    as a list of lists.
    
    Args:
        filename (str): path to the file.

    Returns:
        [[str]] the contents of the fields of the file
    """
    data = []
    with gzip.open(filename) as f:
        for w in f.read():
            data.append(chr(w))

    return list(map(lambda s: s.split('\t'), "".join(data).split('\n')))





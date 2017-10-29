""" Module for reading the sider-files and incorporating them in our Database.
"""
import gzip
from glob import glob
# from MySideEffectApp.models import MeddraFreq


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

    return map(lambda s: s.split('\t'), "".join(data).split('\n'))


name =  [ 'meddra_all_indications.tsv.gz'
        , 'meddra_all_label_indications.tsv.gz'
        , 'meddra_all_label_se.tsv.gz'
        , 'meddra_all_se.tsv.gz'
        , 'meddra_freq.tsv.gz'
        , 'meddra.tsv.gz' ]



def main(filename):

    print(filename)

    for line in read_tsv(filename):
        med = MeddraFreq(
            stitch1 = line[0],
            stitch2 = line[1],
            umls_id = line[2],
            placebo = line[3],
            descrip = line[4],
            freq_hi = line[5],
            freq_lo = line[6],
            meddraC = line[7],
            umlsCon = line[8],
            sideEff = line[9])
        med.save()


# if __name__ == '__main__':
#    main()

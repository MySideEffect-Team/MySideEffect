#!/usr/bin/python3
# -*- coding: iso-8859-15 -*-


from collections import defaultdict, namedtuple
import csv

SideEffect = namedtuple("SideEffect", ["name", "observed"])

tsv_filename = "./sideffect_db.tsv"


drugs_to_sideffects = defaultdict(list)

with open(tsv_filename, "r") as f:
    reader = csv.reader(f, delimiter="\t")
    next(reader, None)

    for row in reader:
        _, drug, _, event, _, _, _, _, observed, *_ = row
        if drug != "ibuprofen":
            continue
        drugs_to_sideffects[drug].append(SideEffect(name=event, observed=int(observed)))

results = drugs_to_sideffects["ibuprofen"]
print(sorted(results, key=lambda se: se.observed))

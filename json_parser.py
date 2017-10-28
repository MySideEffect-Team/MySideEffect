#!/usr/bin/python3
# -*- coding: iso-8859-15 -*-
import json
import argparse

SEXES = {"0": None, "1": "Male", "2": "Female"}


class Occurence(object):
    def __init__(self, gender, age, weight, adverse_effects,
                 literature_reference, country):
        self.gender = gender
        self.age = age
        self.weight = weight
        self.adverse_effects = adverse_effects
        self.literature_reference = literature_reference
        self.country = country


def extract_occurence(line):
    try:
        primary_source = line["primarysource"]
    except KeyError:
        literature_reference = None
    else:
        literature_reference = primary_source.get("literaturereference", None)
        country = primary_source.get("reportercountry", None)

    patient = line["patient"]
    try:
        gender_id = patient["patientsex"]
    except KeyError:
        gender = None
    else:
        gender = SEXES[gender_id]
    age = patient.get("patientonsetage", None)
    weight = patient.get("patientweight", None)

    adverse_effects = [
        reaction["reactionmeddrapt"] for reaction in patient["reaction"]
    ]

    drugs = patient["drug"]

    drug_names = set()

    for drug in drugs:
        try:
            names = drug["openfda"]["generic_name"]
        except KeyError:
            drug_names.add(drug["medicinalproduct"])
        else:
            for name in names:
                drug_names.add(name)

    return Occurence(
        gender=gender, age=age, weight=weight, adverse_effects=adverse_effects,
        literature_reference=literature_reference,
        country=country
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "json_filename"
    )

    args = parser.parse_args()

    with open(args.json_filename, "r") as f:
        data = json.load(f)["results"]

    for line in data:
        print(extract_occurence(line))

if __name__ == "__main__":
    main()

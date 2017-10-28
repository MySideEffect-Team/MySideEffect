#!/usr/bin/python3
# -*- coding: iso-8859-15 -*-
# vim:foldmethod=marker
import json
import argparse

SEXES = {"0": None, "1": "Male", "2": "Female"}


#  CONTINENTSDICT {{{ #
CONTINENTS = {
    "AD": "Europa",
    "AE": "Asia",
    "AF": "Asia",
    "AG": "America",
    "AI": "America",
    "AL": "Europa",
    "AM": "Asia",
    "AN": "America",
    "AO": "Africa",
    "AP": "Asia",
    "AR": "America",
    "AT": "Europa",
    "AW": "America",
    "AX": "Europa",
    "AZ": "Asia",
    "BA": "Europa",
    "BB": "America",
    "BD": "Asia",
    "BE": "Europa",
    "BF": "Africa",
    "BG": "Europa",
    "BH": "Asia",
    "BI": "Africa",
    "BJ": "Africa",
    "BL": "America",
    "BM": "America",
    "BN": "Asia",
    "BO": "America",
    "BR": "America",
    "BS": "America",
    "BT": "Asia",
    "BW": "Africa",
    "BY": "Europa",
    "BZ": "America",
    "CA": "America",
    "CC": "Asia",
    "CD": "Africa",
    "CF": "Africa",
    "CG": "Africa",
    "CH": "Europa",
    "CI": "Africa",
    "CL": "America",
    "CM": "Africa",
    "CN": "Asia",
    "CO": "America",
    "CR": "America",
    "CU": "America",
    "CV": "Africa",
    "CX": "Asia",
    "CY": "Asia",
    "CZ": "Europa",
    "DE": "Europa",
    "DJ": "Africa",
    "DK": "Europa",
    "DM": "America",
    "DO": "America",
    "DZ": "Africa",
    "EC": "America",
    "EE": "Europa",
    "EG": "Africa",
    "EH": "Africa",
    "ER": "Africa",
    "ES": "Europa",
    "ET": "Africa",
    "EU": "Europa",
    "FI": "Europa",
    "FK": "America",
    "FO": "Europa",
    "FR": "Europa",
    "FX": "Europa",
    "GA": "Africa",
    "GB": "Europa",
    "GD": "America",
    "GE": "Asia",
    "GF": "America",
    "GG": "Europa",
    "GH": "Africa",
    "GI": "Europa",
    "GL": "America",
    "GM": "Africa",
    "GN": "Africa",
    "GP": "America",
    "GQ": "Africa",
    "GR": "Europa",
    "GT": "America",
    "GW": "Africa",
    "GY": "America",
    "HK": "Asia",
    "HN": "America",
    "HR": "Europa",
    "HT": "America",
    "HU": "Europa",
    "ID": "Asia",
    "IE": "Europa",
    "IL": "Asia",
    "IM": "Europa",
    "IN": "Asia",
    "IO": "Asia",
    "IQ": "Asia",
    "IR": "Asia",
    "IS": "Europa",
    "IT": "Europa",
    "JE": "Europa",
    "JM": "America",
    "JO": "Asia",
    "JP": "Asia",
    "KE": "Africa",
    "KG": "Asia",
    "KH": "Asia",
    "KM": "Africa",
    "KN": "America",
    "KP": "Asia",
    "KR": "Asia",
    "KW": "Asia",
    "KY": "America",
    "KZ": "Asia",
    "LA": "Asia",
    "LB": "Asia",
    "LC": "America",
    "LI": "Europa",
    "LK": "Asia",
    "LR": "Africa",
    "LS": "Africa",
    "LT": "Europa",
    "LU": "Europa",
    "LV": "Europa",
    "LY": "Africa",
    "MA": "Africa",
    "MC": "Europa",
    "MD": "Europa",
    "ME": "Europa",
    "MF": "America",
    "MG": "Africa",
    "MK": "Europa",
    "ML": "Africa",
    "MM": "Asia",
    "MN": "Asia",
    "MO": "Asia",
    "MQ": "America",
    "MR": "Africa",
    "MS": "America",
    "MT": "Europa",
    "MU": "Africa",
    "MV": "Asia",
    "MW": "Africa",
    "MX": "America",
    "MY": "Asia",
    "MZ": "Africa",
    "NA": "Africa",
    "NE": "Africa",
    "NG": "Africa",
    "NI": "America",
    "NL": "Europa",
    "NO": "Europa",
    "NP": "Asia",
    "OM": "Asia",
    "PA": "America",
    "PE": "America",
    "PH": "Asia",
    "PK": "Asia",
    "PL": "Europa",
    "PM": "America",
    "PR": "America",
    "PS": "Asia",
    "PT": "Europa",
    "PY": "America",
    "QA": "Asia",
    "RE": "Africa",
    "RO": "Europa",
    "RS": "Europa",
    "RU": "Europa",
    "RW": "Africa",
    "SA": "Asia",
    "SC": "Africa",
    "SD": "Africa",
    "SE": "Europa",
    "SG": "Asia",
    "SH": "Africa",
    "SI": "Europa",
    "SJ": "Europa",
    "SK": "Europa",
    "SL": "Africa",
    "SM": "Europa",
    "SN": "Africa",
    "SO": "Africa",
    "SR": "America",
    "ST": "Africa",
    "SV": "America",
    "SY": "Asia",
    "SZ": "Africa",
    "TC": "America",
    "TD": "Africa",
    "TG": "Africa",
    "TH": "Asia",
    "TJ": "Asia",
    "TL": "Asia",
    "TM": "Asia",
    "TN": "Africa",
    "TR": "Europa",
    "TT": "America",
    "TW": "Asia",
    "TZ": "Africa",
    "UA": "Europa",
    "UG": "Africa",
    "US": "America",
    "UY": "America",
    "UZ": "Asia",
    "VA": "Europa",
    "VC": "America",
    "VE": "America",
    "VG": "America",
    "VI": "America",
    "VN": "Asia",
    "YE": "Asia",
    "YT": "Africa",
    "ZA": "Africa",
    "ZM": "Africa",
    "ZW": "Africa",
}

#  }}} CONTINENTSDICT #


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
    print(country)

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

    countries = set()
    for line in data:
        occurence = extract_occurence(line)
        countries.add(CONTINENTS.get(occurence.country, None))

    print(countries)


if __name__ == "__main__":
    main()

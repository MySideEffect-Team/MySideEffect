#!/bin/sh

if [[ $# -lt 1 ]]; then
    echo "USAGE: create_db.sh JSONDIRECTORY"
fi

JSON_DIR="$1"

python3 manage.py shell -c "__import__('openfda_parser').main('"$JSON_DIR"')"

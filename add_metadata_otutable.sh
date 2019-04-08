#!/bin/bash
SCRIPTDIR=$(dirname "$(readlink -f "$0")")
python $SCRIPTDIR"/add_metadata_otutable.py" -im $1 -io $2 -o $3 -t $4 -n $5

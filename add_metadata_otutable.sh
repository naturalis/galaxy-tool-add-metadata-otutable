#!/bin/bash

SCRIPTDIR=$(dirname "$(readlink -f "$0")")
python $SCRIPTDIR"/add_metadata_otutable.py" -im $1 -io $2 -o $3 -t $4 -n $5

# sanity check
printf "Conda env: $CONDA_DEFAULT_ENV\n"
printf "Python version: $(python --version |  awk '{print $2}')\n"
printf "Unzip version: $(unzip -v | head -n1 | awk '{print $2}')\n"
printf "Bash version: ${BASH_VERSION}\n"
printf "SCRIPTDIR: $SCRIPTDIR\n\n"

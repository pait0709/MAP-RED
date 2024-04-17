#!/bin/bash

# Check if the correct number of arguments are provided
if [ "$#" -ne 4 ]; then
    echo "Usage: $0 python_script arg1 arg2 arg3"
    exit 1
fi

# Assign command line arguments to variables
python_script="$1"
arg1="$2"
arg2="$3"
arg3="$4"

# Execute the Python script with the arguments
python3 "$python_script" "$arg1" "$arg2" "$arg3"
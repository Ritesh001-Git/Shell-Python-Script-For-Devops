#!/bin/bash

if [ $# -ne 1 ]; then
    echo "usage: $0 f1.txt"
    exit 1
fi

file=$1

if [ -f "$file" ]; then
    echo "File Name: $file"
    echo "Size: $(du -h "$file")"
    echo "Permission: $(ls -l "$file")"
else 
    echo "File does not exist"
    exit 2 
fi

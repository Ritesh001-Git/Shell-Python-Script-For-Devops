#!/bin/bash

read -p "Enter directory path: " dir

if [ ! -d "$dir" ]; then
    echo "Directory does not exist."
fi

for file in "$dir"/*
do
    echo "$file"
done
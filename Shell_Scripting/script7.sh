#!/bin/bash

read -p "Enter file name: " file

if [ ! -f "$file" ]; then
    echo "File not found"
else
    pwd
fi
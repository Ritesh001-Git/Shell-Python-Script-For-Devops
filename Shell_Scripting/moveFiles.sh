#!/bin/bash

source=$1
dest=$2

echp "moving ...."
mv "$source" "$dest"
echo "Sucessful Moved"
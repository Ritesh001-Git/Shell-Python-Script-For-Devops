#!/bin/bash

read -p "Enter a number: " n
read -p "Enter a number: " k

idx=1
k=$((k + 1))

while [ $idx -lt $k ];
do
    echo "$n * $idx = $((n * idx))"
    idx=$((idx + 1))
done
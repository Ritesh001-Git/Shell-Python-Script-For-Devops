#!/bin/bash

read -a cmd

if command -v "${cmd[0]}" >/dev/null 2>&1; then
    touch p1.log
    "${cmd[@]}" > p1.log
    echo "Command saved sucessfully"
else
    echo "Invalid Command"
fi